#include<iostream>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

int main()
{
    int T,totalcase;
    cin>>T;
    totalcase=T;
    
    while(T)
    {
		int r,c;
		cin>>r>>c;
		
		vector<vector<char> > mat;
		
    	for(int i =0;i<r;i++)
    	{
			vector<char> k;
			char j;
			for(int l =0;l<c;l++)
			{
				cin>>j;
				k.push_back(j);
			}
			mat.push_back(k);
		}
		
		for(int i =0;i<r-1;i++)
		{
			for(int j =0;j<c-1;j++)
			{
				if(mat[i][j]=='#' && mat[i][j+1]=='#'
					&& mat[i+1][j]=='#' && mat[i+1][j+1]=='#')
					{
						mat[i][j]='/';
						mat[i][j+1]= '\\';
						mat[i+1][j] = '\\';
						mat[i+1][j+1]= '/';
					}
			}
		}
		
		int flag =1;
		for(int i =0;i<r;i++)
		{
			for(int j =0;j<c;j++)
			{
				if(mat[i][j]=='#')
				{
					flag =0;
					break;
				}
			}
			if(flag == 0)
			{			cout<<"Case #"<<totalcase -T +1 <<":"<<endl<<"Impossible"<<endl;
				break;
			}
		}

		if(flag == 1)
		{
			cout<<"Case #"<<totalcase -T +1 <<":"<<endl;
			for(int i =0;i<r;i++)
			{
				for(int j =0;j<c;j++)
				{
					cout<<mat[i][j];
				}
				cout<<endl;
			}
		}
            
            
            T--;
    }
    
    return 0;
    
}
