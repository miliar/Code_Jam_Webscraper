#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	int T;
	in>>T;
	bool one = false;
	string s2,s3;
	string prevs2="",prevs3="";
	for (int m=0;m<T;m++){
	int a,b,mx=0;
	bool right = false;
	in>>a>>b;

	for (int i=a; i<b; i++){
			char *s1= new char [0];
			itoa(i,s1,10);
			s2= "";
			for (int k=0;s1[k]!=0;k++)
				s2+=s1[k];
			s3 = s2;
			do {
				if (s3 != s2 && s3[0]!=0){
					
					int z = atoi(s3.c_str());
					if (z<=b && z>a && z>i) {
						for (int zz= 0;zz < s2.length();zz++){
							right = false;
							int len = s2.length()-zz;
							string s4 = s2.substr(zz,s2.length());
							int xx=0;
							for (xx ; xx<len ; xx++){
								if (s4[xx]!=s3[xx]){
									right = true;
									break;
								}
							}
							if (!right){
								for (int hh = 0; hh < s2.length()-s4.length();hh++){
									if (s2[hh]!=s3[xx]){
										right = true;
										break;
									}
									xx++;
								}
							}
							if (!right){
								if (!(prevs2 == s2 && prevs3 == s3)){
									prevs2 = s2; prevs3 = s3;
									//cout << s2 << " : " << s3<<endl;
									mx++;
								}
							}
						}
					}
				}
			}while (next_permutation(s3.begin(),s3.end()));

		}
	out << "Case #"<<m+1<<": "<<mx<<endl;
	}
	return 0;
}
