#include <iostream>
using namespace std;

const int fx[4]={-1,0,0,1};
const int fy[4]={0,-1,1,0};
int tt;
int map[1000][1000];
char cou[1000][1000];
bool bl[1000][1000];
int las[1000][1000];
int main()
    {
        freopen("bl.in","r",stdin);
        freopen("out.txt","w",stdout);
        cin >> tt;
        for (int oo=0; oo<tt; oo++)
            {
                int n,m;
                cin >> n >> m;
                for (int i=0; i<n; i++)
                    for (int j=0; j<m; j++)
                        cin >> map[i][j];
                for (int i=0; i<n; i++)
                    for (int j=0; j<m; j++)
                        {
                            int nx=i;
                            int ny=j;
                            while (true)
                                {
                                    int ki=0;
                                    int lo=map[nx][ny];
                                    for (int x=0; x<4; x++)
                                        {
                                            if ((nx+fx[x]>=0)&&(nx+fx[x]<n)&&
                                            (ny+fy[x]>=0)&&(ny+fy[x]<m)&&
                                            (map[nx+fx[x]][ny+fy[x]]<lo))
                                                {
                                                    ki=x;
                                                    lo=map[nx+fx[x]][ny+fy[x]];
                                                }
                                        }
                                    if ((lo==map[nx][ny]))
                                        {
                                            las[i][j]=nx*10000+ny;
                                            break;
                                        }
                                    nx=nx+fx[ki];
                                    ny=ny+fy[ki];
                                }
                        }
                char now='a';
                memset(bl,0,sizeof(bl));
                for (int i=0; i<n; i++)
                    for (int j=0; j<m; j++)
                        if (bl[i][j]==false)
                            {
                                bl[i][j]=true;
                                cou[i][j]=now;
                                for (int i1=0; i1<n; i1++)
                                    for (int j1=0; j1<m; j1++)
                                        if (las[i][j]==las[i1][j1])
                                            {
                                                bl[i1][j1]=true;
                                                cou[i1][j1]=now;
                                            }
                                now=now+1;
                            }
                cout << "Case #" << oo+1 << ":" << endl;
                for (int i=0; i<n; i++)
                    {
                        for (int j=0; j<m-1; j++)
                            cout << cou[i][j] << " ";
                        cout << cou[i][m-1] << endl;
                    }
            }
    }
