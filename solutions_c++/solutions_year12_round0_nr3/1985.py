#include <iostream>
#include <map>
#include <cmath>
 
using namespace std;
 
typedef unsigned int uint;
 
uint ten_to[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
 
uint countPair(uint key, uint start, uint stop);
 
int main()
{
        uint T;
        uint start, stop, count;
 
        ios_base::sync_with_stdio(false);
        
        cin >> T;
	
        for (uint t = 1; t <= T; ++t)
        {
		count = 0;
		
                cin >> start >> stop;
 
                for(uint key = start; key <= stop; key++)
                {
			count += countPair(key, start, stop);
                }

		cout << "Case #" << t << ": " << count << "\n";
        }
	
        return 0;
}
 
uint countPair(uint key, uint start, uint stop)
{
        uint count = 0;
        uint alternate;
	uint key_len = (uint) log10(key);

	map<uint,bool> hive;
 
        for (uint cut_pos = 1; cut_pos <= key_len; cut_pos++)
        {
		alternate = (key % ten_to[cut_pos]) * ten_to[key_len - cut_pos + 1];

		if (uint(log10(alternate)) != key_len)
			continue;

		alternate += key / ten_to[cut_pos];
 
		if ((alternate >= start) && (alternate <= stop) && (alternate < key) && (hive.count(alternate) == 0))
		{
	                count++;
			hive[alternate] = true;
		}
        }
 
        return count;
}

