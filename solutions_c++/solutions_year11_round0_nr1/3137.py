#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <climits>

using namespace std;

#define eps 1e-6

typedef long long int64;
typedef unsigned long long uint64;

int main()
{
 	freopen("A-large.in", "r", stdin); //input file
	freopen("robotout1.txt", "w", stdout); // output file
	int t, cno = 1;
	scanf("%d",&t);
	while(t--)
	{
			  int n;
			  scanf("%d%*c",&n);
			  vector<int> bn, blno, orno;
			  vector<char> c;

			  for(int i = 0; i < n; i++)
			  {
					  char ch; int no;
					  scanf("%c%*c%d%*c",&ch,&no);
					  c.push_back(ch);
					  bn.push_back(no);
					  if(ch == 'B')blno.push_back(no);
					  if(ch == 'O')orno.push_back(no);
 		  	  }

 		  	  int ans = 0, k = 0;
 		  	  int pos1 = 1, pos2 = 1;
 		  	  int i1 = 0, i2 = 0;
			  int temp1 = -1, temp2 = -1;
			  if(blno.size() != 0)temp1 = blno[0];
			  if(orno.size() != 0)temp2 = orno[0];
 		  	  while(k < n)
  		  	  {
					  char c1 = c[k];
					  if(c1 == 'O')
					  {
                            if(pos2 == temp2 && i2 < orno.size())
                            {
                            if(i2 + 1 < orno.size())temp2 = orno[i2 + 1];
							i2++;
							k++;
							ans++;
							if(pos1 < temp1){pos1++;}
					  		if(pos1 > temp1){pos1--;}
				 			}
							else
							{
                                if(pos2 < temp2){pos2++;}
					  			if(pos2 > temp2){pos2--;}
					  			if(pos1 < temp1){pos1++;}
					  			if(pos1 > temp1){pos1--;}
					  			ans++;
					 		}
		   			  }
		   			  else
		   			  {
							if(pos1 == temp1 && i1 < blno.size())
							{
                             if(i1 + 1 < blno.size())temp1 = blno[i1 + 1];
							 i1++;
							 k++;
							 ans++;
							 if(pos2 < temp2){pos2++;}
					  		 if(pos2 > temp2){pos2--;}
				 			}
				 			else
				 			{
                                if(pos2 < temp2){pos2++;}
					  			if(pos2 > temp2){pos2--;}
					  			if(pos1 < temp1){pos1++;}
					  			if(pos1 > temp1){pos1--;}
					  			ans++;
				 		 	}
		   	  	 	  }
   		   	  }
 		  	  printf("Case #%d: %d\n",cno++,ans);
 	}
	return 0;
}
