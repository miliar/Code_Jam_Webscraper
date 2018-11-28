#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>


using namespace std;

int main()
{
      vector<int> O;
      vector<int> B;
      vector<char> Turns;
      int kases;
      char ch;
      scanf("%d",&kases);
      int tc = 1 , buttons, ans , number;
      int bposB , bposO , toWalkO , toWalkB , cposO , cposB;
      while(tc <= kases)
      {
	    O.clear();
	    B.clear();
	    Turns.clear();
	    ans = 0;
	    scanf("%d",&buttons);
	    for(int i=0 ; i<buttons ; i++)
	    {
		  getchar();
		  scanf("%c%d",&ch,&number);
		  if(ch == 'O')
			O.push_back(number);
		  else
			B.push_back(number);
		  Turns.push_back(ch);

	    }

	    cposO = 1 , cposB = 1;
	    bposO = 0 , bposB = 0;

	    while(bposO + bposB < Turns.size())
	    {

		  if(Turns[bposO + bposB] == 'O')
		  {
			toWalkO = abs(cposO - O[bposO]);
			toWalkB = abs(cposB - B[bposB]);
			ans += toWalkO +1 ; 
			cposO = O[bposO];
			bposO++;
			if(toWalkB <= toWalkO +1)
			      cposB = B[bposB];
			else
			{
			      if(cposB > B[bposB])
				    cposB -= (toWalkO +1);
			      else
				    cposB += (toWalkO +1);
			}

		  }

		  else if(Turns[bposO + bposB] == 'B')
		  {
			toWalkO = abs(cposO - O[bposO]);
			toWalkB = abs(cposB - B[bposB]);
			ans += toWalkB +1 ; 
			cposB = B[bposB];
			bposB++;
			if(toWalkO <= toWalkB +1)
			      cposO = O[bposO];
			else
			{
			      if(cposO > O[bposO])
				    cposO -= (toWalkB +1);
			      else
				    cposO += (toWalkB +1);
			}

		  }



	    }

	    printf("Case #%d: %d\n",tc , ans);

	    tc ++;
      }

}
