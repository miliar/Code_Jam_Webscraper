#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

//void prlist(deque<char> List)
//{
//	printf("[");
//	for (int i=0; i < List.size()-1; i++) {
//		printf("%c, ", List.at(i));
//	}
//	printf("%c]\n", List.back());
//}

void invoke(string &str, map<char,string> &C, map<char,char> &D)
{
    map<char, int> count;
    char ch = 'A';
//    for (int i=0; i < 26; i++) {
//        cout << "C[" << ch << "] = " << C[ch] << endl;
//        ch++;
//    }
    deque<char> List;
    string tmp;
	bool combined = false;
    
    //Start processing input
    for (int i=0; i < str.size(); i++) {

        if(List.empty()) {
            count[str[i]]++;
            List.push_back(str[i]);
            continue;
        }
        
        //See if there's combining scope
        if(C[str[i]] != "" && !List.empty()) {
            tmp = C[str[i]];
            if(tmp[0] == List.back()) {
                count[List.back()]--;
                List.pop_back();
                count[tmp[1]]++;
                List.push_back(tmp[1]);
				continue;
            }
        }
        //Now, if there's a demolition scope
        if(D[str[i]] >= 'A') {
            if (count[D[str[i]]] > 0) {
                count.clear();
				List.clear();
				continue;
            }
        }
		//Otherwise, just add it
		
			count[str[i]]++;
			List.push_back(str[i]);
		
//		prlist(List);
    }
	
	//Now, print the list
	if(!List.empty()) {
		printf("[");
		for (int i=0; i < List.size()-1; i++) {
			printf("%c, ", List.at(i));
		}
		printf("%c]\n", List.back());
	} else {
		printf("[]\n");
	}
}

int main(void)
{
    int T, n;
    map<char, string> C;
    map<char, char> D;
    string str;
    
    scanf("%d", &T);
    for (int i=0; i < T; i++) {
        //Test Case
        
        //Scan C
        scanf("%d", &n);
        for (int j=0; j < n; j++) {
            cin >> str;
            if(str.size()!=3) return -1;
            if (C[str[0]] == "") {
                C[str[0]].append(1,str[1]);
                C[str[0]].append(1,str[2]);
            }
            if (C[str[1]] == "") {
                C[str[1]].append(1,str[0]);
                C[str[1]].append(1,str[2]);
            }
        }
        
        //Scan D
        scanf("%d", &n);
        for (int j=0; j < n; j++) {
            cin >> str;
            if(str.size()!=2) return -1;
            D[str[0]] = str[1];
            D[str[1]] = str[0];
        }
        
        //Scan N
        scanf("%d", &n);
        cin >> str;
        
        //Perform the required operations
        printf("Case #%d: ", i+1);
		invoke(str, C, D);
        
        //Clear Data Structures
        C.clear();
        D.clear();
        str = "";
    }
    return 0;
}