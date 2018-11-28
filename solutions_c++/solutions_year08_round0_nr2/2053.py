#include <iostream>
#include <stdlib.h>
#include <fstream>

int comp(char* t1, char* t2, int t){
	int h1, m1, h2, m2;
	sscanf(t1, "%d:%d", &h1, &m1);
	sscanf(t2, "%d:%d", &h2, &m2);

	m1 += 60*h1;
	m2 += 60*h2;

	if (m1 >= m2 + t)
		return 0;
	else
		return 1;
}

int main() {
	int n, t, na, nb, cases = 1;
	int aCont, bCont;

	std::ofstream outFile("out2", std::ios::out);
	
	char arrival[200][6];
	char departure[200][6];
	char hold[6];
	
	bool marcaArrival[200] = { false };

	std::cin >> n;

	while(n > 0) {
		std::cin >> t;
		std::cin >> na;
		std::cin >> nb;
		aCont = na;
		bCont = nb;
		for (int i = 0; i < na; i++){
			std::cin >> departure[i];
			std::cin >> arrival[i];
		}
			
		for (int i = na; i < na+ nb; i++){
			std::cin >> departure[i];
			std::cin >> arrival[i];
		}

		for (int j = 0; j < na - 1; j++)
			for(int i = 0; i < na - 1; i++){
				if (comp(arrival[i], arrival[i+1], 0) == 0){
					strcpy(hold, arrival[i]);
					strcpy(arrival[i], arrival[i+1]);
					strcpy(arrival[i+1], hold);
				}
				if(comp(departure[i], departure[i+1], 0) == 0){
					strcpy(hold, departure[i]);
					strcpy(departure[i], departure[i+1]);
					strcpy(departure[i+1], hold);

				}
			}

		
		for(int i = na; i  < na+nb -1; i++)
			for (int j = na; j < na+nb-1; j++){
				if (comp(arrival[j], arrival[j+1], 0) == 0){
					strcpy(hold, arrival[j]);
					strcpy(arrival[j], arrival[j+1]);
					strcpy(arrival[j+1], hold);
				}
				if(comp(departure[j], departure[j+1], 0) == 0){
					strcpy(hold, departure[j]);
					strcpy(departure[j], departure[j+1]);
					strcpy(departure[j+1], hold);

				}

			}		
				
		for (int i = 0; i  < na; i++){
			for(int j = na; j < na+nb; j++){
				if (comp(departure[i], arrival[j], t) == 0){
					if (marcaArrival[j] == false ){
						aCont--;
						marcaArrival[j] = true;
						break;
					}
				}
			}
		}

		for (int j = na; j < na+nb; j++){
			for(int i = 0; i < na; i++){					
				if (comp(departure[j], arrival[i], t) == 0){
					if (marcaArrival[i] == false){
						bCont--;
						marcaArrival[i] = true;
						break;
					}

				}
			}
		}
		
		outFile << "Case #" << cases << ": " << aCont << " " << bCont << '\n';
		cases++;
		aCont = 0;
		bCont = 0;
		
		for (int i = 0; i < 200; i++){
			for (int j = 0; j < 6; j++){
				arrival[i][j] = '\0';
				departure[i][j] = '\0';
			}
			marcaArrival[i] = false;
		}
				

		n--;
	}
	
	
	return 0;
}
