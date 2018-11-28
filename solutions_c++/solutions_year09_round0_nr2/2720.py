#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int map[101][101];
char flag[101][101];
vector< pair<int,int> > v;
char f ;
int T,H,W;
ofstream of("2.txt");

void flow(int h,int w);//判断x流向
bool find_max(int &h, int &w);
int main()
{
    
    cin >> T;
    
    for (int l=0; l<T; l++)//T个map
    {
		cin >> H >> W;
		f = 'a';
		
		int maxh=0, maxw=0;
        for (int i=0; i<H; i++)//初始化flag[][]
        {
            for (int j=0; j<W; j++)
            {
                flag[i][j] = '!';
                cin >> map[i][j];
            }
        }


		of << "Case #" << l+1 << ":" << endl;
		flag[0][0] = 'a';
		flow(0,0);
		//for (int i=0; i<H; i++)//处理
        //{
            //for (int j=0; j<W; j++)
            while (1)
            {
				//if (flag[i][j]!='!')continue;
				maxh = 0; maxw = 0;
				if (!find_max(maxh, maxw)) break;
				//if (maxh==0 && maxw==0) flag[0][0] = 'a';
				
				v.clear();
				flow(maxh, maxw);
            }
        //}
        
        for (int i=0; i<H; i++)
        {
			for (int j=0; j<W; j++)
			{
                of << flag[i][j] << ' ';
			}
			of << endl;
		}
    }
	//system("pause");
    return 0;
}


void flow(int h,int w)//判断x流向
{
	//cout << "h=" << h << ",w=" << w << endl;
	int *pmin = &map[h][w];
	char *minf = &flag[h][w];
	pair<int,int> p(h,w);

	int i=h, j=w;
	if (i>0)//North
	{
		i--;
		if (map[i][j] < *pmin) {pmin = &map[i][j]; minf = &flag[i][j]; p = pair<int,int>(i,j);}
	}
	
	i=h; j=w;
	if (j>0)//west
	{
		j--;
        if (map[i][j] < *pmin) {pmin = &map[i][j]; minf = &flag[i][j];p = pair<int,int>(i,j);}
	}
	
	i=h; j=w;
	if (j<W-1)//east
	{
		j++;
		if (map[i][j] < *pmin) {pmin = &map[i][j]; minf = &flag[i][j];p = pair<int,int>(i,j);}
	}
	
	i=h; j=w;
	if (i<H-1)//south
	{
		i++;
        if (map[i][j] < *pmin) {pmin = &map[i][j]; minf = &flag[i][j];p = pair<int,int>(i,j);}
	}

	
	
	//标记
	if (map[h][w] == *pmin)//周围没有比此地小
	{
		//if (flag[h][w] != '!') continue;
		if (flag[h][w] == '!')
		{
			if (h==0 && w==0) flag[h][w] = 'a';
			else 
			{
				f = f+1;
				flag[h][w] = f;
			}
			int len = v.size();
			for (int i=0; i<len; i++)
			{
				//of << "\n(" << v[i].first << "," << v[i].second << ")" << endl;
				flag[v[i].first][v[i].second] = flag[h][w];
			}
		}
	}
	else//周围有比此地小的地方
	{
		if (flag[h][w]!='!')
		{
			*minf = flag[h][w];
			flow(p.first, p.second);
		}
		else
		{
			v.push_back(pair<int,int>(h,w));
			if (flag[p.first][p.second]!='!')
			{
                int len = v.size();
				for (int i=0; i<len; i++)
				{
					//of << "\n(" << v[i].first << "," << v[i].second << ")" << endl;
					flag[v[i].first][v[i].second] = flag[p.first][p.second];
				}
			}
			else flow(p.first, p.second);
		}
		
	}

}

bool find_max(int &h, int &w)
{
	int min = -1;
	for (int i=0; i<H; i++)
	{
		for (int j=0; j<W; j++)
		{
			if (flag[i][j] != '!') continue;
			if (map[i][j] > min)
			{
				min = map[i][j];
				h = i;
				w = j;
			}
		}
	}
	if (min==-1) return false;
	else return true;
}

