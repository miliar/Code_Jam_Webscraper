#include <QFile>
#include <QTextStream>

//Artem Klimov's solution
//soved using Qt Framework 4.7.1

//idea:  every robot spends (K + 1) seconds to solve (O/B K) task ("walk and press").
//  robots can walk at simultaneously (and have to do it to make time minimum), even when one is walking to some distance button, while
//  other presses several nessessary buttons, but they shouldn't press buttons together


QFile inFile("C:/CodeJam0/A-small-attempt0.in");
QFile outFile("C:/CodeJam0/output.txt");


void PressButton(QList<int> &pressingRobotTasks, int &pressingRobotPosition, QList<int> &walkingRobotTasks, int &walkingRobotPosition, int &sTime)
{
	int timeForOneTask = abs(pressingRobotTasks[0]-pressingRobotPosition) + 1;	//1sec to press
	sTime += timeForOneTask;
	pressingRobotPosition = pressingRobotTasks[0];		//move robot to the position
	pressingRobotTasks.removeFirst();		//his task is done

	//now, at the same time second robot is allowed to walk timeForOneTask*1 meters
	if(walkingRobotTasks.count()==0) return;  //no more tasks for walking robot

	int walkVector = walkingRobotTasks[0]-walkingRobotPosition;
	if( abs(walkVector) <= timeForOneTask )		//enough to move to the pos
	{
		walkingRobotPosition = walkingRobotTasks[0];
	}
	else	//walk as far as can (or stay)
	{
		if(walkVector>0) walkingRobotPosition += timeForOneTask*1;
		if(walkVector<0) walkingRobotPosition -= timeForOneTask*1;
	}
}

int main(int argc, char *argv[])
{
	inFile.open(QFile::ReadOnly);
	outFile.open(QFile::WriteOnly);
	QTextStream inData(&inFile);
	QTextStream outData(&outFile);

	int T;
	inData >> T;

	for(int t=0; t<T; t++)
	{
		int N;
		inData >> N;

		QList<int> orangeTasks, blueTasks;
		QList<char> buttonsOrder;	//to save order in which they need to press

		for(int i=0; i<N; i++)
		{
			char type=' ';
			while(type==' ') inData >> type;
			int buttonNumb;
			inData >> buttonNumb;
			if(type=='O')	orangeTasks.append(buttonNumb);
			else			blueTasks.append(buttonNumb);

			buttonsOrder.append(type);
		}

		int oPosition=1, bPosition=1;	//current robot positions
		int sTime=0;		//current time

		while( buttonsOrder.count() )
		{
			if(buttonsOrder[0]=='O')	//orange needs to press now
				PressButton(orangeTasks, oPosition, blueTasks, bPosition, sTime);
			else						//blue needs to press
				PressButton(blueTasks, bPosition, orangeTasks, oPosition, sTime);

			buttonsOrder.removeFirst();
		}

		outData << QString("Case #%1: %2").arg(t+1).arg(sTime);
		outData << "\r\n";
	}
}