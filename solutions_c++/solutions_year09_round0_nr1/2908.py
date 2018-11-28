#include<iostream>
#include<string>
using namespace std;
const int N = 5001;
string dic[N];
int len, d, n;
bool in[20][27];

int main()
{
   // freopen("s.in","r",stdin);
   // freopen("s.out","w",stdout);
    int i,j,k;
    cin>>len>>d>>n;
    for(i=0;i<d;i++)
        cin>>dic[i];
     cin.ignore();    
    for(i=1;i<=n;i++)
    {
        memset(in,0,sizeof(in));
        char ch;
        int all = -1;
       
        while(ch=cin.get())
        {
           // cout<<ch<<"dfsfdsf\n";
            ++all;
            if(ch == '\n') break;
            if(ch=='(')
                while(cin>>ch&&ch!=')')
                    in[all][ch-'a'] = true;
            else
                in[all][ch-'a'] = true;
        }

        int res = 0;
        for(j=0;j<d;j++)
        {
            for(k=0;k<len;k++)
                if(in[k][dic[j][k]-'a'] == false)
                    break;
            if(k==len)
                res++;
        }
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    //;system("pause");
    return 0;
}
