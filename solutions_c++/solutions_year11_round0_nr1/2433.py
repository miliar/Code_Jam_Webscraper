#include <cstdio>
#include <map>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>
#include <cmath>
#include <iostream>
#include <utility>

using namespace std;

int main (){

	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.out", "w+");
    int n;
	fscanf (fin, "%d\n", &n);
	char buff[2000];
	vector <pair <string, int> > v;
	vector <int> orange,blue;
	int p1, p2;

	for (int i = 0; i < n; i++){
	    int final = 0;
	    p1 = p2 = 1;
	    v.clear();
	    orange.clear();
	    blue.clear();
        fgets (buff, sizeof(buff), fin);
        string s = (string)buff;
        s+= " ";
        int where = -1;
        string robot = "";
        string tmp = "";
        int o = 0, b = 0;
        for (int j = 0; j < s.length(); j++){
            if (s[j] == ' '){
                if (where == -1){
                    tmp = "";
                    where++;
                }
                else if (where == 0){
                    robot = tmp;
                    where++;
                    tmp = "";
                }
                else if (where == 1){
                    int a;
                    sscanf (tmp.c_str(), "%d", &a);
                    v.push_back(make_pair(robot, a));
                    if (robot == "O"){
                        orange.push_back(a);
                    }
                    else blue.push_back(a);
                    where = 0;
                    tmp = "";
                }
            }
            else tmp += s[j];
        }

        for (int j = 0; j < v.size(); j++){
            //printf ("%d %d %d\n", i+1, j, final);
            //printf ("%d %s %d\n",j, v[j].first.c_str(), v[j].second);
            s = v[j].first;
            int a = v[j].second;
            //printf ("%s %d\n", s.c_str(), a);
            if (s == "O"){
                int time = abs(a - p1) + 1;
                final += time;
                p1 = a;
                o++;
                if (p2 != blue[b]){
                    if (p2 < blue[b]){
                        p2 += time;
                        if (p2 > blue[b]){
                            p2 = blue[b];
                        }
                    }
                    else {
                        p2 -= time;
                        if (p2 < blue[b]) p2 = blue[b];
                    }
                }
            }
            else if (s == "B"){
                int time = abs(a - p2) + 1;
                final += time;
                p2 = a;
                b++;
                if (p1 != orange[o]){
                    if (p1 < orange[o]){
                        p1 += time;
                        if (p1 > orange[o]){
                            p1 = orange[o];
                        }
                    }
                    else {
                        p1 -= time;
                        if (p1 < orange[o]) p1 = orange[o];
                    }
                }
            }
        }
        fprintf (fout, "Case #%d: %d\n", i+1, final);
	}

	//system ("PAUSE");
	return 0;
}
