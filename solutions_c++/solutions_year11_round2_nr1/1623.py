// a.exe < int.txt > out.txt

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <list>
#include <set>
#include <map>

int main(int argc, char* argv[])
{
	int num_of_cases;
	std::cin >> num_of_cases;
	for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
		int num_of_teams;
		std::cin >> num_of_teams;
		std::vector<std::vector<char> > tbl(num_of_teams, std::vector<char>(num_of_teams));
		std::vector<int> wins(num_of_teams, 0);
		std::vector<int> loses(num_of_teams, 0);
		for (int team_num_y = 0; team_num_y < num_of_teams; ++team_num_y) {
			int win = 0, los = 0;
			for (int team_num_x = 0; team_num_x < num_of_teams; ++team_num_x) {
				std::cin >> tbl[team_num_y][team_num_x];
				if (tbl[team_num_y][team_num_x] == '1') {
					wins[team_num_y]++;
				}
				else if (tbl[team_num_y][team_num_x] == '0') {
					loses[team_num_y]++;
				}
			}
		}
		// OWP (Opponents' Winning Percentage) is the average WP of all your opponents,
		//   after first throwing out the games they played against you.
		// For example, if you throw out games played against team D,
		//   then team B has WP = 0 and team C has WP = 0.5.
		// Similarly, team A has OWP = 0.5,
		//            team B has OWP = 0.5,
		//        and team C has OWP = 2/3.
		// Therefore  team D has OWP = 0.5 * (0 + 0.5) = 0.25.
		std::vector<double> owps(num_of_teams, 0.0);
		for (int team_num_y = 0; team_num_y < num_of_teams; ++team_num_y) {
			int op = 0;
			for (int team_num_x = 0; team_num_x < num_of_teams; ++team_num_x) {
				if (tbl[team_num_y][team_num_x] == '.')
					continue;
				int win = wins[team_num_x];
				int los = loses[team_num_x];
				if (tbl[team_num_x][team_num_y] == '1') {
					win--;
					op++;
				}
				else if (tbl[team_num_x][team_num_y] == '0') {
					los--;
					op++;
				}
				if (win + los != 0)
					owps[team_num_y] += (double) win / ((double) win + los);
			}
			if (op != 0)
				owps[team_num_y] /= op;
		}
		std::cout << "Case #" << case_num << ": " << std::endl;
		for (int team_num_y = 0; team_num_y < num_of_teams; ++team_num_y) {
			double rpi = 0.0;
			if (wins[team_num_y] + loses[team_num_y] != 0)
				rpi += 0.25 * (double) wins[team_num_y] / ((double) wins[team_num_y] + loses[team_num_y]);
			double oowps = 0.0;
			int op = 0;
			for (int team_num_x = 0; team_num_x < num_of_teams; ++team_num_x) {
				if (tbl[team_num_x][team_num_y] == '1' || tbl[team_num_x][team_num_y] == '0') {
					oowps += owps[team_num_x];
					op++;
				}
			}
			if (op != 0)
				oowps /= op;
			rpi += 0.5 * owps[team_num_y] + 0.25 * oowps;
			printf("%0.12f\n", rpi);
//			std::cout << rpi << std::endl;
		}
	}
	return 0;
}

