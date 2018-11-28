#include <cstdio>
#include <map>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>
#include <cmath>
#include <iostream>
#include <utility>
#include <stack>

using namespace std;

vector <string> split (char * buff, char c){
    string temp = "";
    string s = (string)buff + " ";
    vector <string> v;
    for (int i = 0; i < s.length(); i++){
        if (s[i] == c){
            v.push_back(temp);
            temp = "";
        }
        else temp += s[i];
    }
    return v;
}

int main (){

	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("B-output.out", "w+");
	int casenum;
	fscanf (fin, "%d\n", &casenum);
	map <string, int> counter;
	map <string, string> combine;
	map <string, vector<string> > destroy;

	for (int k = 0; k < casenum; k++){
	    counter.clear();
	    combine.clear();
	    destroy.clear();
        char buff[30000];
        fgets(buff, sizeof(buff), fin);
        vector <string> v = split (buff, ' ');
        int c, d, n;
        /*for (int i = 0; i < v.size(); i++){
            printf ("%s\n", v[i].c_str());
        }*/
        sscanf (v[0].c_str(), "%d", &c);
        for (int i = 1; i <= c; i++){
            string temp = "";
            temp += v[i][0];
            temp += v[i][1];
            string novi = "";
            novi += v[i][2];
            combine[temp] = novi;
            //printf ("combine %s -> %s\n", temp.c_str(), novi.c_str());
            temp = "";
            temp += v[i][1];
            temp += v[i][0];
            combine[temp] = novi;
            //printf ("combine %s -> %s\n", temp.c_str(), novi.c_str());
        }
        sscanf (v[c+1].c_str(), "%d", &d);
        for (int i = c+2; i <= c+d+1; i++){
            string prvi, drugi;
            prvi = drugi = "";
            prvi += v[i][0];
            drugi += v[i][1];
            destroy[prvi].push_back(drugi);
            destroy[drugi].push_back(prvi);
        }
        sscanf (v[c+d+2].c_str(), "%d", &n);
        string s = v[c+d+3];
        //printf ("%s\n", s.c_str());
        stack <string> castlist;
        string temp = "";
        string last = "";
        for (int i = 0; i < s.length(); i++){
            temp = "";
            temp += s[i];
            if (temp == "\n") continue;
            if (castlist.empty()){
                castlist.push(temp);
                //printf ("   case 1\n");
                counter[temp] = 1;
                continue;
            }
            last = "";
            last += castlist.top();
            //printf ("t %s l %s *%s*\n",temp.c_str(), last.c_str(), (temp+last).c_str());
            if (combine.find(temp+last) != combine.end()){
                //printf ("   case 2\n");
                //counter[temp]--;
                counter[last]--;
                castlist.pop();
                castlist.push(combine[temp+last]);
                continue;
            }
            for (int j = 0; j < destroy[temp].size(); j++){
                string oopsie = "";
                oopsie += destroy[temp][j];
                if (counter.find(oopsie)!= counter.end()){
                    if (counter[oopsie] == 0) continue;
                    //printf ("   case 3\n");
                    while(!castlist.empty()) castlist.pop();
                    counter.clear();
                    break;
                }
            }
            if (castlist.empty()) continue;
            //printf ("   %s %s\n", temp.c_str(), last.c_str());
            castlist.push(temp);
            if (counter.find(temp) == counter.end()) counter[temp] = 1;
            else counter[temp]++;
        }
        stack <string> final;
        while (!castlist.empty()){
            final.push(castlist.top());
            castlist.pop();
        }
        fprintf (fout, "Case #%d: [", k+1);
        while (!final.empty()){
            temp = final.top();
            final.pop();
            fprintf (fout, "%s", temp.c_str());
            if (!final.empty()) fprintf (fout, ", ");
        }
        fprintf (fout, "]\n");
	}


	system ("PAUSE");
	return 0;
}
