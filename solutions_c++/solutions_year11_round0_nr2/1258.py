#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>


int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "B-large.in", "r");
	fopen_s(&Out, "B-large.out", "w");

	int nTestCases, iTestCase;
	char str[1000];
	//char st[1000];
	char s[1000];
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		int i=0, j;
		int table[30][30];
		int table_1[30][30];
		for (i=0;i<30;i++) {
			for (j=0;j<30;j++) {
				table[i][j] = 0;
				table_1[i][j] = 0;
			}
		}

		i=0;

		fscanf_s(In, "%s", &str);
		int num1 = atoi(str);
		for (j = 0; j < num1; j++) {
			fscanf_s(In, "%s", &str);
			table[str[i]-65][str[i+1]-65] = str[i+2]-65;
			table[str[i+1]-65][str[i]-65] = str[i+2]-65;
		}
		fscanf_s(In, "%s", &str);
		int num2 = atoi(str);
		for (j = 0; j < num2; j++) {
			fscanf_s(In, "%s", &str);
			table_1[str[i]-65][str[i+1]-65] = -1;
			table_1[str[i+1]-65][str[i]-65] = -1;
		}
		fscanf_s(In, "%s", &str);
		int num3 = atoi(str);

		fscanf_s(In, "%c", &str[i]);
		for (i=0;i<num3;i++)
			fscanf_s(In, "%c", &str[i]);
		//fscanf_s(In, "%s", &str);

		//fscanf_s(In, "%s", &str);
		//char *sn;
		//sn = "";
		//while (str[i] != ' ') {
		//	sn += str[i];
		//	i++;
		//}
		//int num1 = atoi(sn);
		//i++;
		//for (j = 0; j < num1; j++) {
		//	table[str[i]-65][str[i+1]-65] = str[i+2]-65;
		//	table[str[i+1]-65][str[i]-65] = str[i+2]-65;
		//	i+=4;
		//}

		//sn = "";
		//while (str[i] != ' ') {
		//	sn += str[i];
		//	i++;
		//}
		//int num2 = atoi(sn);
		//i++;
		//for (j = 0; j < num2; j++) {
		//	table[str[i]-65][str[i+1]-65] = -1;
		//	table[str[i+1]-65][str[i]-65] = -1;
		//	i+=3;
		//}

		//sn = "";
		//while (str[i] != ' ') {
		//	sn += str[i];
		//	i++;
		//}
		//int num3 = atoi(sn);
		//i++;
		//for (j = 0; j < num3; j++) {
		//	st[j] = str[i];
		//	i++;
		//}

		i=0;
		for (j = 0; j < num3; j++) {
			s[i] = str[j];
			if (i>0 && table[s[i]-65][s[i-1]-65] > 0) {
				s[i-1] = table[s[i]-65][s[i-1]-65]+65;
				continue;
			}
			for (int k=0; k<i; k++) {
				if (table_1[s[i]-65][s[k]-65] == -1) {
					i=-1;
					break;
				}
			}
			i++;
		}

		//Write Out Results
		fprintf_s(Out, "Case #%d: [", iTestCase+1);
		for (j=0;j<i;j++) {
			if (j==0) 
				fprintf_s(Out, "%c", s[j]);
			else
				fprintf_s(Out, ", %c", s[j]);
		}
		fprintf_s(Out, "]\n");

	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
