/*
 * AlienLanguage.cpp
 *
 *  Created on: Sep 4, 2009
 *      Author: akshay
 */

#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main() {
	int l, d, n;
	const int lineSize = 15 * 28 + 1;
	char line[lineSize];
	char letter[15][26];
	
	cin>>l>>d>>n;
	
	//	Consume end of line
	cin.getline(line, lineSize);

	char language[d][l+1];
	for(int i=0; i<d; i++) {
		cin.getline(language[i], l+1);
		for(int j=0; j<l; j++)
			language[i][j] -= 'a';
	}
	
	for(int cno=0; cno<n; cno++) {
		memset(letter, '\0', 15 * 26);
		cin.getline(line, lineSize);
		
		int lno = 0;
		bool multi = false;
		for(char *p = line; *p != '\0'; p++) {
			if(multi) {
				if(*p==')') {
					multi = false;
					lno++;
				} else
					letter[lno][*p - 'a'] = 1;
			} else {
				if(*p=='(')
					multi = true;
				else
					letter[lno++][*p - 'a'] = 1;
			}
		}
		
		int cnt = 0;
		for(int i=0; i<d; i++) {
			bool contains = true;
			for(int j=0; j<l && contains; j++) {
				if(letter[j][(int)language[i][j]] == 0)
					contains=false;
			}
			
			if(contains)
				cnt++;
		}
		
		cout<<"Case #"<<(cno+1)<<": "<<cnt<<endl;
	}
	
	return EXIT_SUCCESS;
}
