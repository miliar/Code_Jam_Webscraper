#include<iostream>
#include<string>
#include<vector>
#include<queue>

using namespace std;
class Point
{
    public:
    int x, y;
};
int main()
{
	int tot, cn, caseCount=0;
	int i,j,k,x,y,H,W,min;
	Point p;
	int land[100][100];
	char basin[100][100],cur;
	Point to[100][100];
	vector< Point > from[100][100], pv;
	queue<vector < Point > > q;


	cin >> tot;
	for(cn=0;cn<tot;++cn)
	{
	    //i/p & process
		cin >> H >> W;
		for(i=0;i<H;++i)
		{
		    for(j=0;j<W;++j)
		    {
		        cin >> land[i][j];
		        basin[i][j]='X';
		        from[i][j].clear();
		    }
		}

		//Find flow from & to:
		for(i=0;i<H;++i)
		{
		    for(j=0;j<W;++j)
		    {
		        x=y=-1;
		        min=land[i][j];
		        if(i && land[i][j]>land[i-1][j] && min>land[i-1][j])
		            min=land[x=i-1][y=j];
                if(j && land[i][j]>land[i][j-1] && min>land[i][j-1])
		            min=land[x=i][y=j-1];
                if(j<W-1 && land[i][j]>land[i][j+1] && min>land[i][j+1])
		            min=land[x=i][y=j+1];
                if(i<H-1 && land[i][j]>land[i+1][j] && min>land[i+1][j])
		            min=land[x=i+1][y=j];
                p.x=x;p.y=y;
                to[i][j]=p;
                if(x!=-1)
                {
                    p.x=i;p.y=j;
                    from[x][y].push_back(p);
                }
		    }
		}

//		for(i=0;i<H;++i)
//		{
//		    for(j=0;j<W;++j)
//		    {
//		        cout << "{(" << to[i][j].x << "," << to[i][j].y << ")[";
//		        for(k=0;k<from[i][j].size();++k)
//                    cout << "(" << from[i][j][k].x << "," << from[i][j][k].y << ")";
//                cout << "]}";
//		    }
//		    cout << endl;
//		}

        cur='a';
		for(i=0;i<H;++i)
		{
		    for(j=0;j<W;++j)
		    {
		        if(basin[i][j]!='X')
                    continue;

                x=i;y=j;
		        while(x!=-1)
		        {
		            //cout << "(" << x << "," << y << ")";
		            basin[x][y]=cur;
		            q.push(from[x][y]);
		            p=to[x][y];
		            x=p.x;y=p.y;
		        }
		        //cout << "|";


		        while(!q.empty())
		        {
		            pv=q.front();
		            if(!pv.empty())
		            {
		                for(k=0;k<pv.size();++k)
                        {
                            p=pv[k];
		                    if(basin[p.x][p.y]=='X')
		                    {
                                basin[p.x][p.y]=cur;
                                q.push(from[p.x][p.y]);
                                //cout << "(" << p.x << "," << p.y << ")";
		                    }
		                }
		            }
		            q.pop();
		        }
		        //cout << endl;
		        ++cur;
		    }
		}

	    cout << "Case #" << ++caseCount << ": " << endl;
        for(i=0;i<H;++i,cout<<endl)
            for(j=0;j<W;++j)
                cout << basin[i][j] << " ";
	}
	return 0;
}
