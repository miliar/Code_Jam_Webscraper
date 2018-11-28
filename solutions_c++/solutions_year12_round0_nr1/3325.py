#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<string>

using namespace std;
int main(int argc, char* argv[])
{
    int test_case;
    string in,out;
    int alp[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    int alg[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
    freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
	cin>>test_case;
	getline(cin,in);
	for(int i=0;i<test_case;i++)
    {
        getline(cin,in);
        for(int j=0;j<in.length();j++)
        {
            char a=in[j],b;
            int pos;
            if(a!=' ')
            {
                for(int k=0;k<26;k++)
                {
                    if(alg[k]==a)
                    {
                    pos=k;
                    b=alp[pos];
                    out+=b;
                    break;
                    }
                }
            }
            else
                out+=' ';
        }
        in="";
        cout<<"Case #"<<(i+1)<<": "<<out<<endl;
        out="";
    }
}

