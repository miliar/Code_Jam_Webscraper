#include "stdafx.h"
#include<iostream>
using namespace std;
struct button{
	int target;
	int tag;
};
int main()
{
	struct button *blue = new button[200];
	struct button *oran = new button[200];
	int T, N, temp, count_o, count_b, count;
	int pos_o, pos_b, cur_o, cur_b, visited, aim, times;
	int result;
    char color;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        cin >> N;
		count_o = count_b = count =0;
        for(int j = 0; j < N; j++)
        {
            cin >> color >> temp;
            if(color=='O')
            {
				oran[count_o].target = temp;
				oran[count_o++].tag = count++;
            }
            if(color=='B')
            {
				blue[count_b].target = temp;
				blue[count_b++].tag = count++;
            }
        }
		pos_o = pos_b = 1;
		cur_o = cur_b = 0;
		visited = result = 0;
        while(visited < count){
			if(cur_o < count_o && oran[cur_o].tag == visited)
            {
                result += abs(oran[cur_o].target - pos_o) + 1;
                for(int j = 0; j < abs(oran[cur_o].target - pos_o) + 1; j++)
                {
					if(pos_b < blue[cur_b].target)
                        pos_b++;
					else if(pos_b == blue[cur_b].target)
                        break;
                    else if(pos_b > blue[cur_b].target)
                        pos_b--;
                }
				pos_o = oran[cur_o].target;
				cur_o++;
				visited++;
            }
			if(cur_b < count_b && blue[cur_b].tag == visited){
				result += abs(blue[cur_b].target - pos_b) + 1;
				for(int j = 0; j < abs(blue[cur_b].target - pos_b) + 1; j++)
				{
					if(pos_o < oran[cur_o].target)
						pos_o++;
					else if(pos_o == oran[cur_o].target)
						break;
					else if(pos_o > blue[cur_o].target)
						pos_o--;
				}
				pos_b = blue[cur_b].target;
				visited++;
				cur_b++;
			}
        }
        cout<< "Case #"<< i + 1<< ": " << result << endl;
    }
	return 0;
}
