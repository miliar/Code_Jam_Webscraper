#include<iostream>
#include<fstream>

using namespace std;

char mat[110][110];
int n,num[110],win[110];
double wp[110],owp[110],oowp[110];

int main()
{
    int t,k=0,i,j;
    ifstream cin("A-large.in");
    ofstream cout("a.out");
    cin>>t;
    while(t--)
    {
    	cin>>n;
    	for(i=0;i<n;++i)
    	{
    		num[i]=win[i]=0;
    		for(j=0;j<n;++j)
    		{
    			cin>>mat[i][j];
    			if(mat[i][j]=='1')
    				++win[i];
				else if(mat[i][j]=='0')
					++num[i];
    		}
    		num[i]+=win[i];
    		wp[i]=double(win[i])/double(num[i]);

    	}
    	for(i=0;i<n;++i)
    	{
    		owp[i]=0;
    		for(j=0;j<n;++j)
    		{
    				if(mat[j][i]=='1')
    					owp[i]+=double(win[j]-1)/double(num[j]-1);
					else if(mat[j][i]=='0')
						owp[i]+=double(win[j])/double(num[j]-1);

    		}
    		owp[i]=owp[i]/double(num[i]);
    	}
    	for(i=0;i<n;++i)
    	{
    		oowp[i]=0;
    		for(j=0;j<n;++j)
    		{
    			if(mat[i][j]!='.')
    			{
    				oowp[i]+=owp[j];
    			}
    		}
    		oowp[i]/=double(num[i]);
    	}
    	cout<<"Case #"<<++k<<":"<<endl;
    	for(i=0;i<n;++i)
    	{
    		cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
    	}

    }


    return 0;
}
