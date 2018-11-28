#include<iostream>
#include<string>
using namespace std;

int main()
{
    int N,S,Q;
    char se[100][101],query[1000][101],enter[2];
    int count[100],m=0,switchea=0;

    cin>>N;
    
    for(int i=0;i<N;i++) //read test cases
    {
        cin>>S;
		cin.getline(enter,2);
        for(int j=0;j<S;j++) //read search engines
        {
                cin.getline(se[j],100,'\n');
        }
        
        cin>>Q;
		cin.getline(enter,2);
        for(int k=0;k<Q;k++)
        {
                cin.getline(query[k],100,'\n'); 
        }  
		switchea=0;
		m=0;
		while(m<Q)
		{
			for(int n=0;n<S;n++)
				count[n] = Q;

			for(int s=0;s<S;s++)
			{
				for (int q=m;q<Q;q++)
				{
				    if(strcmp(se[s],query[q])==0)
					{
						count[s] = q;
						break;
					}
				}
			}

			m = count[0];      
	        for(int c=1;c<S;c++)
		    {
			        if(m<count[c])
				    {
					     m = count[c];
					}        
			}
		
			if (m<Q)
				switchea++;
		}
        
        cout<<"Case #"<<i+1<<": "<<switchea<<"\n";
    }
    
    
    
    return 0;
}