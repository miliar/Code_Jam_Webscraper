
#include <stdio.h>
#include <vector>

class CRobot{
public :
	CRobot()
		: m_Time(0)
		, m_Pos(1)
	{

	}

	void setStatus(int pos, int time)
	{
		m_Pos=pos;
		m_Time=time;

	}
	int getPos(){return m_Pos;}
	int getTime(){return m_Time;}
private:
	int m_Time;
	int m_Pos;
};

int main(int argc, char* argv[])
{

	freopen("c:\\input.in","r",stdin);
	freopen("C:\\output.txt","w",stdout);

	int T = 0;

	scanf("%d", &T);

	for(int t = 0 ; t < T ; t++)
	{
		CRobot botOran;
		CRobot botBlue;

		int N = 0 ;
		scanf("%d", &N);

		int timeCur = 0;

		for(int n = 0 ; n< N ; n++)
		{
			char robot[2];
			int buttonPos ;
			scanf("%s", robot);
			scanf("%d", &buttonPos );

			CRobot *pActionBot = NULL;
			if(robot[0] == 'O')
				pActionBot = &botOran;
			else
				pActionBot = &botBlue;

			int timeAdd = 0;
			int timeFree = timeCur - pActionBot->getTime();
			int timeReq = buttonPos - pActionBot->getPos();
			timeReq = (timeReq < 0)? -timeReq:timeReq;

			if(timeReq > timeFree)
			{
				timeCur+= (timeReq - timeFree + 1);
				
			}
			else
			{
				timeCur++;
			}
			
			pActionBot->setStatus(buttonPos, timeCur);

		}		

		printf("Case #%d: %d\n", t+1, timeCur);
	}

	return 0;
}