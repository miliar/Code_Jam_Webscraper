#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
using std::vector;
char dic[10005][11];
char charlst[105];
int charbit[10005];
int len[10005];
int main()
{
	FILE* infid = fopen("ss.in","r");
	FILE* outfid = fopen("ss.out","w");
	int cases;
	int n,m;
	fscanf(infid,"%d",&cases);
	for(int cc=1; cc<=cases; ++cc)
	{
		fscanf(infid,"%d%d",&n,&m);
		for(int i=0;i<n; ++i)
		{
			fscanf(infid,"%s",dic[i]);
			charbit[i] = 0;
			len[i] = strlen(dic[i]);
			for(int j=0; j<len[i]; ++j)
			{
				charbit[i] |= 1<<(dic[i][j]-'a');
			}			
		}
		fprintf(outfid,"Case #%d:",cc);
		
		for(int i=0;i<m; ++i)
		{
			int maxscore = 0;
			int id = 0;
			fscanf(infid,"%s",charlst);
			for(int j=0; j<n; ++j)
			{
			
				vector<int>cur_lst;
				int cur_bit = 0;
				int score = 0;
				for(int k=0; k<n; ++k)
				{
					if(len[j] == len[k])
					{
						cur_lst.push_back(k);
						cur_bit |= charbit[k];
					}
				}
				for(int tk=0; tk<26; ++tk)
				{
					int chark = charlst[tk]-'a';
					if(cur_lst.size() <= 1)break;
					if((cur_bit & (1<<chark)) == 0)continue;
					vector<int>new_cur_lst;
					int new_cur_bit = 0;
					if(((1<<chark) & (charbit[j])) == 0)
					{
						++score;
						for(int s=0; s<cur_lst.size(); ++s)
						{
							if((charbit[cur_lst[s]] & (1<<chark)) == 0)
							{
								new_cur_lst.push_back(cur_lst[s]);
								new_cur_bit |= charbit[cur_lst[s]];
							}
						}
						cur_lst.clear();
						cur_lst = new_cur_lst;
						cur_bit = new_cur_bit;						
						continue;
					}
					else
					{
						for(int s=0; s<cur_lst.size(); ++s)
						{
							bool ok = true;
							for(int t=0; t<len[j]; ++t)
							{
								if(dic[j][t] == chark+'a' && dic[cur_lst[s]][t]!=chark+'a')
								{
									ok = false;
								}
								if(dic[j][t] !=chark+'a' && dic[cur_lst[s]][t]==chark+'a')
								{
									ok = false;
								}
							
							}
							if(ok)
							{
								new_cur_lst.push_back(cur_lst[s]);
								new_cur_bit |= charbit[cur_lst[s]];
							}	
						}
						cur_lst.clear();
						cur_lst = new_cur_lst;
						cur_bit = new_cur_bit;		
					}										
				}
				if(score > maxscore)
				{
					maxscore = score;
					id = j;
				}
			}
			fprintf(outfid," %s",dic[id]);
		}
		fprintf(outfid,"\n");
		
	}
	fclose(infid);
	fclose(outfid);
	return 0;
}
