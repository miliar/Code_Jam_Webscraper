#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
struct nodo
{
    int x,y,cost;
    nodo(int _x,int _y,int _cost)
    {
        x=_x;
        y=_y;
        cost=_cost;    
    }
};
char ad[101][101];
bool visited[101][101];
int c[101][101];
int R,C;
int di[4]={-1,0,0,1};
int dj[4]={0,-1,1,0};
vector<int> hijo(int x,int y)
{
    int minx=1000;
    int miny=1000;
    int minal=c[x][y];
    for(int i=0;i<4;i++)
    {
        int X=x+di[i];
        int Y=y+dj[i];
        if(X>=0 && X<R && Y>=0 && Y<C)
            if(c[X][Y]<minal)
            {
                minal=c[X][Y];
                minx=X;
                miny=Y;    
            }
            else if(c[X][Y]==minal)
            {
                if(X<minx){minx=X;miny=Y;}    
                    else if(X==minx && Y<miny)miny=Y;
            }          
    }
    vector<int>v;
    if(minal!=c[x][y])
    {v.push_back(minx);v.push_back(miny);}
    return v;
}
int main()
{
 //   freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int n;
    cin>>n;
    for(int ana=0;ana<n;ana++)
    {
        cin>>R>>C;
        ad[0][0]='a';
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
                cin>>c[i][j],visited[i][j]=0;
        queue<nodo>Q;
        int conta=0;
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
            if(!visited[i][j])
            {
                Q.push(nodo(i,j,conta));
                visited[i][j]=1;
                ad[i][j]='a'+conta;
              //  cout<<"xx "<<i<<" "<<j<<endl;
                conta++;
                while(!Q.empty())
                {
                    nodo h = Q.front();
                    int x=h.x;
                    int y=h.y;
                    int cost=h.cost;
                    Q.pop();
                    //hijos
                    vector<int>c=hijo(x,y);
                    if(c.size()==2)
                        if(!visited[c[0]][c[1]])
                        {
                            Q.push(nodo(c[0],c[1],cost));
                            visited[c[0]][c[1]]=1;
                            ad[c[0]][c[1]]='a'+cost;
                         //   cout<<c[0]<<" "<<c[1]<<endl;
                        }
                    //padres    
                    
                  //  cout<<"aaaa  "<<x<<" "<<y<<endl;
                    for(int i=0;i<4;i++)
                    {
                        int X=x+di[i];
                        int Y=y+dj[i];
                        if(X>=0 && X<R && Y>=0 && Y<C)
                        if(!visited[X][Y])
                        {
                            vector<int>hamlet=hijo(X,Y);
                            if(hamlet.size()==2)
                            if(hamlet[0]==x && hamlet[1]==y)
                            {
                                Q.push(nodo(X,Y,cost));
                                visited[X][Y]=1;
                                ad[X][Y]='a'+cost;
                       //         cout<<X<<" -"<<Y<<endl;
                            }
                        }
                     //   cout<<"          "<<i<<endl;
                    }
                }
            }
        cout<<"Case #"<<ana+1<<":"<<endl;
        for(int i=0;i<R;i++)
        {   
            for(int j=0;j<C;j++)
            if(j!=C-1)
                cout<<ad[i][j]<<" ";
            else    
                cout<<ad[i][j];
            cout<<endl;
        }
    }
    //system("pause");
    return 0;
}


