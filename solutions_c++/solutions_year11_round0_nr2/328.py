#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int a[1001];

int main()
{
	int t;   
	int n;
	
    cin >> t;
    
    for(int tt=1; tt<=t; tt++)
    {
		int c, d, n;
		string res;
		string now;
		
		cin >> c;
		vector<string> com(c);
		for(int i=0; i<c; i++) cin >> com[i];
		
		cin >> d;
		vector<string> opp(d);
		for(int i=0; i<d; i++) cin >> opp[i];
		
		cin >> n >> now;
		
		while(n > 0)
		{	
			char ch1 = now[0];
			now.erase(now.begin());	
			n--;
			
			bool ok = false;
						
			if (res.size() > 0)
			{
				char ch2 = res[res.size() - 1];				

				for(int i=0; i<c; i++)
				{
					
					if ((com[i][0] == ch1 && com[i][1] == ch2) || (com[i][0] == ch2 && com[i][1] == ch1))
					{								
						res[res.size() - 1] = com[i][2];
						ok = true;
						break;
					}					
				}
			}
			
			if (ok) continue;
						
			for(int i=0; i<opp.size(); i++)
			{
				if (opp[i][0] == ch1)
				{
					for(int j=0; j<res.size(); j++)
					{
						if (opp[i][1] == res[j])
						{
							res.clear();
							ok = true;
							break;
						}
					}
					if (ok) break;
				}
				else if (opp[i][1] == ch1)
				{
					for(int j=0; j<res.size(); j++)
					{
						if (opp[i][0] == res[j])
						{
							res.clear();
							ok = true;
							break;
						}
					}
					if (ok) break;
				}						
			}
			
			if (ok) continue;

			res += ch1;
		}
		printf("Case #%d: [", tt);
		for(int i=0; i<res.size(); i++)
		{
			if (i > 0) printf(", ");
			printf("%c", res[i]);
		}
		printf("]\n");
    }
    return 0;
}
