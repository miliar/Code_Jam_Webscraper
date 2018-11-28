#include <iostream>
#include <vector>
int main(){

	int cases = 0;
	std::cin >> cases;
	for (int i = 1; i < cases+1; i++) {
		int buttons = 0;
		std::vector<std::pair<char,int> > sequence;
		std::vector<std::pair<char,int> > orange;
		std::vector<std::pair<char,int> > blue;
		std::cin >> buttons;
		for (int j = 0; j < buttons; j++) {
			char robot = '\0';
			int button = 0;
			std::cin >> robot;
			std::cin >> button;
			sequence.push_back(std::pair<char,int>(robot, button));
			if (robot == 'O') {
				orange.push_back(std::pair<char,int>(robot, button));
			}else if (robot == 'B') {
				blue.push_back(std::pair<char,int>(robot, button));
			}

		}
		std::vector<std::pair<char,int> > ::iterator iter = sequence.begin();
		std::vector<std::pair<char,int> > ::iterator oiter = orange.begin();
		std::vector<std::pair<char,int> > ::iterator biter = blue.begin();

		int o =1, b =1, time = 0;
		int otime = 0, btime = 0;
		while (oiter != orange.end()) {
			otime+=abs(oiter->second-o)+1;
			if (oiter->second!=o) {
				o=oiter->second;
			}
			oiter->second = otime;
			oiter++;
		}
		while (biter != blue.end()) {
			btime+=abs(biter->second-b)+1;
			if (biter->second!=b) {
				b=biter->second;
			}
			biter->second = btime;
			biter++;
		}
		
		oiter = orange.begin();
		biter = blue.begin();
		
		while (iter != sequence.end()) {
			std::vector<std::pair<char,int> > ::iterator temp = iter-1;
			int penalty = 0;
			if (iter->first == 'O') {
				if (iter != sequence.begin() && temp->first != 'O' && temp->second >= oiter->second) {
					penalty = temp->second - oiter->second;
					penalty++;
				}
				std::vector<std::pair<char,int> > ::iterator otemp = oiter;
				while (otemp != orange.end()) {
					otemp->second+=penalty;
					otemp++;
				}
				iter->second = oiter->second;
				oiter++;
			}else if (iter->first == 'B') {
				if (iter != sequence.begin() && temp->first != 'B' && temp->second >= biter->second) {
					penalty = temp->second - biter->second;
					penalty++;
				}
				std::vector<std::pair<char,int> > ::iterator btemp = biter;
				while (btemp != blue.end()) {
					btemp->second+=penalty;
					btemp++;
				}
				iter->second = biter->second;
				biter++;
			}
			iter++;
		}
	
		printf("Case #%i: %i\n", i, (iter-1)->second);
	}

	return 0;
}