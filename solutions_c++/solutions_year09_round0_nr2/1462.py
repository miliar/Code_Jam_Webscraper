#include <iostream>
#include <vector>

using namespace std;

int H, W;
char c;
int M[100][100];
char color[100][100];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

void dfs(int i, int j)
{
    color[i][j] = c;
    
    int minH = M[i][j];
    int downI = -1, downJ = -1;
        
    for(int k=0; k<4; k++)
    {
        int I = i + dx[k];
        int J = j + dy[k];
        
        if(I>=0 && I<H && J>=0 && J<W && M[I][J] < minH)
        {
            minH = M[I][J];
            downI = I;
            downJ = J;
        }
        
    }
    if(downI != -1 && color[downI][downJ]==0) dfs(downI, downJ);
    
    for(int k=0; k<4; k++)
    {
        int I = i + dx[k];
        int J = j + dy[k];
        
        if(I>=0 && I<H && J>=0 && J<W)
        {
            int minH = M[I][J];
            int downI = -1, downJ = -1;
            
            for(int w=0; w<4; w++)
            {
                int II = I + dx[w];
                int JJ = J + dy[w];
                
                if(II>=0 && II<H && JJ>=0 && JJ<W && M[II][JJ] < minH)
                {
                    minH = M[II][JJ];
                    downI = II;
                    downJ = JJ;
                }
            }
            if(downI == i && downJ == j && color[I][J] == 0) dfs(I, J);
        }
    }    
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin>>T;
    
    for(int nCaso = 1; nCaso <= T; nCaso++)
    {
        cin>>H>>W;
        
        for(int i=0; i<H; i++)
            for(int j=0; j<W; j++)
                cin>>M[i][j];
        
        memset(color, 0, sizeof(color));
        
        c = 'a';
        for(int i=0; i<H; i++)
        {
            for(int j=0; j<W; j++)
            {
                if(color[i][j]==0)
                {
                    dfs(i, j);
                    c++;
                }
            }
        }
        
        cout<<"Case #"<<nCaso<<":"<<endl;
        for(int i=0; i<H; i++)
        {
            cout<<color[i][0];
            for(int j=1; j<W; j++)
                cout<<" "<<color[i][j];
            cout<<endl;
        }
    }
    return 0;
}
