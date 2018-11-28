#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	FILE *fp;
	fp = fopen("output.txt","w");
	int T = 1;
	scanf("%d\n",&T);
	for(int i=1; i<=T; i++) {
		string buf;
		int j=0;
		getline(cin,buf);
		fprintf(fp,"Case #%d: ",i);
		for(int j=0; j<buf.length(); j++) {
			switch (buf[j]) {
				case 'y' : buf[j] = 'a';  break;
				case 'n' : buf[j] = 'b';  break;
				case 'f' : buf[j] = 'c';  break;
				case 'i' : buf[j] = 'd';  break;
				case 'c' : buf[j] = 'e';  break;
				case 'w' : buf[j] = 'f';  break;
				case 'l' : buf[j] = 'g';  break;
				case 'b' : buf[j] = 'h';  break;
				case 'k' : buf[j] = 'i';  break;
				case 'u' : buf[j] = 'j';  break;
				case 'o' : buf[j] = 'k';  break;
				case 'm' : buf[j] = 'l';  break;
				case 'x' : buf[j] = 'm';  break;
				case 's' : buf[j] = 'n';  break;
				case 'e' : buf[j] = 'o';  break;
				case 'v' : buf[j] = 'p';  break;
				case 'z' : buf[j] = 'q';  break;
				case 'p' : buf[j] = 'r';  break;
				case 'd' : buf[j] = 's';  break;
				case 'r' : buf[j] = 't';  break;
				case 'j' : buf[j] = 'u';  break;
				case 'g' : buf[j] = 'v';  break;
				case 't' : buf[j] = 'w';  break;
				case 'h' : buf[j] = 'x';  break;
				case 'a' : buf[j] = 'y';  break;
				case 'q' : buf[j] = 'z';  break;
			}
			fprintf(fp,"%c",buf[j]);
		}
		fprintf(fp,"\n");
		
	}
	return 0;
}	