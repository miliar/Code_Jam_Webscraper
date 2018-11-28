// Magik

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;

int main()
{
	//freopen("B-large.in", "r",stdin);
	//freopen("out_lr.txt","w", stdout);
	int t, cno = 1;
	scanf("%d",&t);
	while(t--)
	{
			  int n_comb, n_opp;
			  scanf("%d",&n_comb);
			  string comb[n_comb];
			  for(int i = 0; i < n_comb; ++i)
			          cin >> comb[i];
			  scanf("%d",&n_opp);
			  string opp[n_opp];
			  for(int i = 0; i < n_opp; ++i)
			          cin >> opp[i];

			  int sz;
			  string inp;
			  scanf("%d",&sz);
			  cin >> inp;
			  //cout << sz << " " << inp << endl;
			  string ans = "";
			  for(int i = 0; i < sz; ++i)
			  {
					  char ch = inp[i];
					  if(ans.size() == 0){ans.append(1, ch); continue;}
					  char ch1 = ans[ans.size() - 1];
					  bool is_comb = false, is_opp = false;;
					  // test for comb
					  for(int p = 0; p < n_comb; ++p)
					  {
					if((comb[p][0] == ch && comb[p][1] == ch1) || (comb[p][0] == ch1 && comb[p][1] == ch))
								   {
								   ans[ans.size() - 1] = comb[p][2];
								   is_comb = true;
								   }
   		  			  }
					  if(!is_comb)
					  {
								  // test for opp
						  for(int q = 0; q < n_opp; q++)
						  {
						  for(int r = 0; r < ans.size() && ans.size() != 0; ++r)
						  {
	  			  if((opp[q][0] == ch && opp[q][1] == ans[r]) || (opp[q][0] == ans[r] && opp[q][1] == ch))
	  			                {ans = "";
	  			                is_opp = true;}
								}
	   		  			  }

  			  		  }
  			  		  if(!is_opp && !is_comb)ans.append(1, ch);
 		  	  }
 		      if(ans.size() == 0)
 		      {
                            printf("Case #%d: []\n", cno++);
                            continue;
			  }
 		  	  printf("Case #%d: [", cno++);
			  for(int i = 0; i + 1 < ans.size() ; ++i)
			          {
			          printf("%c, ", ans[i]);
					  }
			  printf("%c]\n", ans[ans.size() - 1]);
	}
	return 0;
}
