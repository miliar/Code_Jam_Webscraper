#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
	char alphabet[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int T;
	freopen("A-small-attempt3.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	getchar();
	int count = 1;
	while (T--) {
		char temp;
		char result[101];
		int iter = 0;
		while ((temp = getchar()) != '\n') {
			if ((temp-'a') >= 0 && (temp-'a') <= 26) {
				result[iter++] = alphabet[temp - 'a'];
			} else {
				result[iter++] = temp;
			}
		}
		cout<<"Case #"<<count++<<": ";
		for (int i = 0; i < iter; i++){
			cout<<result[i];
		}
		cout<<endl;
	}
	return 0;
}