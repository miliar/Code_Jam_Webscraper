#include <iostream>
using namespace std;
int main()
{
    int mark[26][26],i,j,k,l,m,c,d,n,r,total,con,start;
    char imark[26][26];
    string a,b,s;
    char ss[101];
    cin>>m;
    for (j=1;j<=m;j++)
    {
        memset(imark,0,sizeof(imark));
        memset(mark,0,sizeof(mark));
        cin>>c;
        for (k=1;k<=c;k++) 
        {
            cin>>a;
            imark[a[0]-'A'][a[1]-'A']=a[2];
            imark[a[1]-'A'][a[0]-'A']=a[2];
        }
        cin>>d;
        for (k=1;k<=d;k++) 
        {
            cin>>b;
            mark[b[0]-'A'][b[1]-'A']=1;
            mark[b[1]-'A'][b[0]-'A']=1;
        }
        cin>>n;
        cin>>s;
        start=0;r=0;
        for (k=0;k<n;k++)
        {
            if (k>0)
            {
                if (s[k-1]==' ')
                {
                    r++;
                    ss[r]=s[k];
                    continue;
                }
                if (imark[s[k-1]-'A'][s[k]-'A'])
                {
                    ss[r]=imark[s[k-1]-'A'][s[k]-'A'];
                    s[k]=' ';s[k-1]=' ';
                    continue;
                }
                con=0;
                for (l=start;l<k;l++)
                {
                    if (s[l]==' ') continue;
                    if (mark[s[k]-'A'][s[l]-'A'])
                    {
                        r=0;
                        s[k]=' ';
                        start=k+1;
                        con=1;
                        break;
                    }
                }
                if (con) continue;
            }
            r++;
            ss[r]=s[k];
        }
        cout<<"Case #"<<j<<": [";
        for (k=1;k<r;k++) cout<<ss[k]<<", ";
        if (r>0) cout<<ss[r];
        cout<<"]"<<endl;
    }
}
                
                
