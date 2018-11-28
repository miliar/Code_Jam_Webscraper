#include<iostream>
using namespace std;
int o[101];
int p[101];
int out[101];
int main()
{
	freopen("A.txt", "w", stdout);
	int t , n , temp , all , l;
	char in;
	int place_o , place_p , all_o , all_p;
	int now_o , now_p;
	cin >> t;
	for(l = 0 ; l < t; l++)
	{
		cin >> n;
		place_o = place_p = 0;
		for(temp = 0; temp < n; temp ++)
		{
			cin >> in;
			if(in == 'O')
			{
				cin >> o[place_o ++];
				out[temp] = 0;
			}
			else
			{
				cin >> p[place_p ++];
				out[temp] = 1;
			}
		}
		all_o = place_o , all_p = place_p;
		place_o = place_p = all = temp = 0;
		now_p = now_o = 1;
		while(place_o < all_o && place_p < all_p)
		{
			if(out[temp] == 0)
				if(now_o < o[place_o])
				{
					now_o ++;
					all++;
					if(now_p < p[place_p])
						now_p++;
					else if(now_p > p[place_p])
						now_p--;
				}
				else if(now_o > o[place_o])
				{
					now_o --;
					all++;
					if(now_p < p[place_p])
						now_p++;
					else if(now_p > p[place_p])
						now_p--;
				}
				else
				{
					place_o++;
					all++;
					temp++;
					if(now_p < p[place_p])
						now_p++;
					else if(now_p > p[place_p])
						now_p--;
				}
			else
				if(now_p < p[place_p])
				{
					now_p ++;
					all++;
					if(now_o < o[place_o])
						now_o++;
					else if(now_o > o[place_o])
						now_o--;
				}
				else if(now_p > p[place_p])
				{
					now_p --;
					all++;
					if(now_o < o[place_o])
						now_o++;
					else if(now_o > o[place_o])
						now_o--;
				}
				else
				{
					place_p++;
					all++;
					temp++;
					if(now_o < o[place_o])
						now_o++;
					else if(now_o > o[place_o])
						now_o--;
				}
		}
		if(place_o < all_o)
		{
			while(place_o < all_o)
			{
				if(now_o < o[place_o])
				{
					now_o ++;
					all++;
				}
				else if(now_o > o[place_o])
				{
					now_o --;
					all++;
				}
				else
				{
					place_o++;
					all++;
				}
			}
		}
		else if(place_p < all_p)
		{
			while(place_p < all_p)
			{
				if(now_p < p[place_p])
				{
					now_p ++;
					all++;
				}
				else if(now_p > p[place_p])
				{
					now_p --;
					all++;
				}
				else
				{
					place_p++;
					all++;
				}
			}
		}
		cout << "Case #" << l + 1 << ": " << all << endl;
	}
	return 0;
}