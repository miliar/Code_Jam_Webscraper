#include <iostream>
#include <vector>
#include <utility>


using namespace std;

vector<pair<int,int> > pares;

int main()
{
    int casos,n;
	int a,b,c,d,resp;
	
	
	cin>>casos;
	for(int i=1; i<=casos;i++)
    {
		resp=0;
        cin>>n;
		pares=vector<pair<int, int> >(n);
		for(int c=0; c<n ; c++){
			cin>>a>>b;
			pares[c]=make_pair(a,b);
		}
		
		//ordeno
		
		sort(pares.begin(),pares.end());
		//calculo
        for(int a=0; a<n; a++){
			for(int b=a+1; b<n ; b++){
				if(pares[a].second>pares[b].second) resp++;
			}
		}
		//imprimo
		cout<<"Case #"<<i<<": "<<resp<<endl;
	}

    
    
    return 0;    
}
