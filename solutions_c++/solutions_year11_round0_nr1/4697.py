/*
ID: miro.fc1
PROG:
LANG: C++
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int counter = 1, T, N, temp, cur_B, cur_O, ind_ch, ind_B, ind_O;
	char cha;
	vector<char> ch;
	vector<int> O, B;
	cin >> T;
	bool flag, lol;
	while(T--)
	{
	    flag = 0;
	    ind_ch = 0;
	    ind_B = 0;
	    ind_O = 0;
	    cur_B = 1;
	    cur_O = 1;
	    cin >> N;
	    ch.clear();
	    O.clear();
	    B.clear();
	    ch.resize(N);
	    for(int i = 0;i < N;i++)
	    {
            cin >> cha;
            if(cha == 'O')
            {
                ch[i] = 'O';
                cin >> temp;
                O.push_back(temp);
            }
            else
            {
                ch[i] = 'B';
                cin >> temp;
                B.push_back(temp);
            }
	    }
	    int i = 0;
        for(;;i++)
	    {
	        lol = 0;
	        flag = 0;
	        if(ind_O < O.size()){
	        if(O[ind_O] > cur_O /*&& ind_O <= O.size() */)
                cur_O++;
            else if(O[ind_O] < cur_O /*&& ind_O <= O.size() */)
                cur_O--;
            else if(O[ind_O] == cur_O && ch[ind_ch] == 'O'/* && ind_O <= O.size() - 1 && ind_ch < ch.size() - 1*/)
            {
                ind_O++;
                ind_ch++;
                lol = 1;
                //continue;
            }
            }
	        else flag = 1;

	        if(ind_B < B.size()){
            if(B[ind_B] > cur_B /*&& ind_B < B.size() */)
                cur_B++;
            else if(B[ind_B] < cur_B /*&& ind_B < B.size() */)
                cur_B--;
            else if(B[ind_B] == cur_B && ch[ind_ch] == 'B' && !lol/* && ind_B <= B.size() - 1 && ind_ch < ch.size() - 1*/)
            {
                ind_B++;
                ind_ch++;
                //continue;
            }
            }
	        else if(flag)   break;

	    }
	    cout << "Case #" << counter << ": " << i << endl;
        counter++;
	}
	return 0;
}
