#include <iostream>
using namespace std;

int l,n,m;
char str[6000][700];
char stn[6000][700];
int len[700];

int main()
    {
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
          cin >> l >> n >> m;
          for (int i=0; i<n; i++)
            {
                for (int j=0; j<l; j++)
                    cin >> str[i][j];
            }
          for (int i=0; i<m; i++)
            {
                bool flag=false;
                int an=0;
                int now=0;
                int ss=0;
                while (now<l)
                    {
                        cin >> stn[ss][now];
                        ss=ss+1;
                        len[now]=ss;
                        if ((flag==false)&&(!(stn[ss-1][now]=='(')))
                            {
                                now=now+1;
                                ss=0;
                            }
                        else
                            {
                                if (stn[ss-1][now]=='(')
                                    {
                                        flag=true;
                                    }
                                else
                                    {
                                        if (stn[ss-1][now]==')')
                                            {
                                                now++;
                                                ss=0;
                                                flag=false;
                                            }
                                    }
                            }
                    }
                for (int j=0; j<n; j++)
                    {
                        int ok=true;
                        for (int x=0; x<l; x++)
                            {
                                flag=false;
                                for (int k=0; k<len[x]; k++)
                                    {
                                        if (stn[k][x]==str[j][x])
                                            {
                                                flag=true;
                                                break;
                                            }
                                    }
                                if (flag==false)
                                    {
                                        ok=false;
                                        break;
                                    }
                            }
                        if (ok==true)
                            an=an+1;
                    }
                cout << "Case #" << i+1 << ": " << an << endl;
            }
    }
