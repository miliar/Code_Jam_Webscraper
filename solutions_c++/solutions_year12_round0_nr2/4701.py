#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream in ("B-large.in");
	ofstream ven ("ven2.out");
	
	int stevilo;
	in >> stevilo;
	
	for(int a(0);a<stevilo;a++){
		int ponovi, krneki, naj, KolikoJeNaj(0);
		in >> ponovi >> krneki >> naj;
		
		for(int b(0);b<ponovi;b++){
			int temp;
			in >> temp;
			if(temp==0 and naj > 0)continue;
			switch(temp%3){
				case 0:
					temp /= 3;
					if(temp >= naj)KolikoJeNaj++;
					else if(temp+1 >= naj and krneki >0){
						KolikoJeNaj++;
						krneki--;
					}
					break;
				case 1:
					temp /=3;
					if(temp+1 >= naj)KolikoJeNaj++;
					break;
				case 2:
					temp /=3;
					if(temp+1 >= naj)KolikoJeNaj++;
					else if(temp+2 >= naj and krneki >0){
						KolikoJeNaj++;
						krneki--;
					}
					break;
			}
		}
		ven << "Case #" << a+1 << ": " << KolikoJeNaj << endl;
	}
	return 0;
}
