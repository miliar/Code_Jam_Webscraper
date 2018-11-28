#include <iostream>
#include <vector>

int nCases;

int nTime;
int nOrders;
std::vector<int> vOrder;		// 0 : orange; 1 : blue
std::vector<int> vRobotOrders[2];

void reset()
{
	nTime = 0;
	vOrder.clear();
	vRobotOrders[0].clear();
	vRobotOrders[1].clear();
}

void read_input()
{
	std::cin >> nOrders;
	for (int i = 0; i < nOrders; i++)
	{
		char robot;
		int nButton;
		int iRobot;
		std::cin >> robot;
		std::cin >> nButton;
		
		iRobot = (robot == 'B') ? 1 : 0;
		vOrder.push_back(iRobot);
		vRobotOrders[iRobot].push_back(nButton);
	}
}

void solve_input()
{
	int nRobotButtonState[2] = {1, 1};

	std::vector<int>::iterator itNextRobotButton[2] = {vRobotOrders[0].begin(), vRobotOrders[1].begin()};
	for (int iOrder = 0; iOrder < nOrders; iOrder++)
	{
		int iRobot = vOrder[iOrder];
		int iOtherRobot = (iRobot + 1) % 2;
		int nTimeToComplete = abs(*itNextRobotButton[iRobot] - nRobotButtonState[iRobot]) + 1;
		nRobotButtonState[iRobot] = *itNextRobotButton[iRobot];
		if (itNextRobotButton[iOtherRobot] != vRobotOrders[iOtherRobot].end())
		{
			if (abs(*itNextRobotButton[iOtherRobot] - nRobotButtonState[iOtherRobot]) <= nTimeToComplete)
			{
				nRobotButtonState[iOtherRobot] = *itNextRobotButton[iOtherRobot];
			}
			else
			{
				nRobotButtonState[iOtherRobot] += (*itNextRobotButton[iOtherRobot] > nRobotButtonState[iOtherRobot]) ? nTimeToComplete : -nTimeToComplete;
			}
		}
		itNextRobotButton[iRobot]++;
		nTime += nTimeToComplete;
	}
}

void print_solution(int nCase)
{
	std::cout << "Case #" << (nCase + 1) << ": " << nTime << std::endl;
}

int main()
{
	std::cin >> nCases;
	for (int i = 0; i < nCases; i++)
	{
		reset();
		read_input();
		solve_input();
		print_solution(i);
	}
	return 0;
}
