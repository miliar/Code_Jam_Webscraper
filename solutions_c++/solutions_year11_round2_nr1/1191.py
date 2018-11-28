#include <iostream>
#include <vector>
#include <list>

struct Team
{
	std::list<int> wins;
	std::list<int> losses;
	
	double wp;
	double owp;
	double oowp;
};

void calculate_wp(unsigned int team, std::vector<Team>& teams)
{
	Team& t = teams[team];
	
	t.wp = t.wins.size() / double(t.wins.size() + t.losses.size());
}

void calculate_owp(unsigned int team, std::vector<Team>& teams)
{
	Team& t = teams[team];
	
	std::list<int> temp_wins;
	std::list<int> temp_losses;
	
	std::list<int> opponents;
	
	opponents.insert(opponents.begin(), t.wins.begin(), t.wins.end());
	opponents.insert(opponents.begin(), t.losses.begin(), t.losses.end());

	t.owp = 0;
	for (auto i = opponents.begin(); i != opponents.end(); i++)
	{
		temp_wins = teams[*i].wins;
		temp_losses = teams[*i].losses;
		
		temp_wins.remove(team);
		temp_losses.remove(team);
		
		t.owp += temp_wins.size() / double(temp_wins.size() + temp_losses.size());
	}
	
	t.owp /= opponents.size();
}

void calculate_oowp(unsigned int team, std::vector<Team>& teams)
{
	Team& t = teams[team];
	
	std::list<int> opponents;
	
	opponents.insert(opponents.begin(), t.wins.begin(), t.wins.end());
	opponents.insert(opponents.begin(), t.losses.begin(), t.losses.end());
	
	t.oowp = 0;
	for (auto i = opponents.begin(); i != opponents.end(); i++)
	{
		t.oowp += teams[*i].owp;
	}
	
	t.oowp /= opponents.size();
}

void calculate_rpi(unsigned int team, std::vector<Team>& teams)
{
	Team& t = teams[team];
	
	std::cout << t.wp / 4 + t.owp / 2 + t.oowp / 4 << std::endl;
}

void read_matches()
{
	unsigned int number_of_teams = 0;
	std::cin >> number_of_teams;
	
	std::vector<Team> teams;
	teams.resize(number_of_teams);
	
	for (unsigned int i = 0; i < number_of_teams; i++)
	{
		for (unsigned int j = 0; j < number_of_teams; j++)
		{
			char c;
			std::cin >> c;
			if (c == '0') {teams[i].losses.push_back(j);}
			if (c == '1') {teams[i].wins.push_back(j);}
		}
	}
	
	for (unsigned int i = 0; i < number_of_teams; i++) {calculate_wp(i, teams);}
	for (unsigned int i = 0; i < number_of_teams; i++) {calculate_owp(i, teams);}
	for (unsigned int i = 0; i < number_of_teams; i++) {calculate_oowp(i, teams);}
	for (unsigned int i = 0; i < number_of_teams; i++) {calculate_rpi(i, teams);}
}

main()
{
	unsigned int num_tests = 0;
	std::cin >> num_tests;
	
	for (int i = 0; i < num_tests; i++)
	{
		std::cout << "Case #" << i+1 << ": " << std::endl;
		read_matches();
	}
	
	return 0;
}
