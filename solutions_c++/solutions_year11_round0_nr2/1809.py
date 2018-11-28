#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;

int main()
{
    int c,t,d,i,j,k=0,m,len,ss,pos;
    bool flag,frm;
	char ans[110];
    char form[40][5];
    char opp[30][3];
    char str[110];

	ifstream cin("B-large.in");
	ofstream cout("B-large.out");

    cin>>t;
    while(t--)
    {
    	cin>>c;
    	for(i=0;i<c;++i)
    	{
    		cin>>form[i];
    	}
    	cin>>d;
    	for(i=0;i<d;++i)
    	{
    		cin>>opp[i];
    	}
    	cin>>len;
    	cin>>str;

		ans[0]=str[0];
		pos=1;
    	for(i=1;i<len;++i)
    	{
    		frm=true;
    		for(j=0;j<c;++j)
    		{
    			if(!frm) break;

    			if(form[j][0]==str[i]&&ans[pos-1]==form[j][1]||form[j][1]==str[i]&&ans[pos-1]==form[j][0])
    			{
    				frm=false;
    				ans[pos-1]=form[j][2];

    				flag=true;
    				while(flag&&pos>1)
    				{
    					flag=false;
    					for(m=0;m<c;++m)
    					{

    						if(form[m][0]==ans[pos-2]&&ans[pos-1]==form[m][1]||form[m][1]==ans[pos-2]&&ans[pos-1]==form[m][0])
							{
    							flag=true;
    							--pos;
    							ans[pos-1]=form[m][2];
    						}
    					}
    				}
    			}
    		}
    		if(frm)
    		{
    			ans[pos]=str[i];
    			++pos;
    		}
    		if(pos>1)
    		{
    			for(j=0;j<d;++j)
    			{
    				if(ans[pos-1]==opp[j][0])
    				{
    					for(ss=0;ss<pos-1;++ss)
    					{
    						if(ans[ss]==opp[j][1])
    						{
    							pos=0;
    							break;
    						}
    					}
    				}
    				else if(ans[pos-1]==opp[j][1])
    				{
    					for(ss=0;ss<pos-1;++ss)
    					{

							if(ans[ss]==opp[j][0])
							{
								pos=0;
								break;

							}
    					}
    				}
    			}

    		}
    	}
    	ans[pos]='\0';
    	cout<<"Case #"<<++k<<": ";
    	if(pos==0)
    	{
    		cout<<"[]"<<endl;
    	}
    	else{
    		cout<<"["<<ans[0];
    		for(i=1;i<pos;++i)
				cout<<", "<<ans[i];
			cout<<"]"<<endl;
    	}
    }

    return 0;
}
