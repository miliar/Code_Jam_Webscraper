#include <iostream>
#include <sstream>
#include <math.h>


#define UInt32 unsigned long int


struct Robot {
	short	actualPosition;
	UInt32	lastUsedSecond;

	Robot () :
		actualPosition (1),
		lastUsedSecond (0)
	{
	}

};


void PressButton (const short buttonToPress, Robot& robot, UInt32& lastUsedSecond);


int main ()
{
	UInt32		numberOfCases	= 0;
	UInt32		counter			= 0;
	
	std::cin >> numberOfCases;
	
	while (counter < numberOfCases) {
		short	buttonsToPress;
		Robot	orangeRobot;
		Robot	blueRobot;
		UInt32	lastUsedSecond = 0;

		std::cin >> buttonsToPress;

		for (short i = 0; i < buttonsToPress; ++i) {
			char	robot;
			short	buttonToPress;

			std::cin >> robot;
			std::cin >> buttonToPress;

			if (robot == 'O')
				PressButton (buttonToPress, orangeRobot, lastUsedSecond);
			else
				PressButton (buttonToPress, blueRobot, lastUsedSecond);
		}

		std::cout << "Case #" << ++counter << ": " << lastUsedSecond << std::endl;
	}
}


inline void PressButton (const short buttonToPress, Robot& robot, UInt32& lastUsedSecond)
{
	UInt32 secondsToPress = std::abs (buttonToPress - robot.actualPosition) + 1;

	lastUsedSecond = std::max (robot.lastUsedSecond + secondsToPress, lastUsedSecond + 1);
	
	robot.actualPosition = buttonToPress;
	robot.lastUsedSecond = lastUsedSecond;
}