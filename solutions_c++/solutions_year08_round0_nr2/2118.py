#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main(int argc, char** argv)
{
	if(argc != 2)
		return 0;

	ifstream file;

	file.open(argv[1]);
	if(!file.is_open())
		return 0;

	int N = 0;
	string line;

	getline(file, line);
	N = atoi(line.c_str());

	for(int i=1; i<=N; i++)
	{
		int turnTime = 0;

		/* get the turn around time */
		getline(file, line);
		turnTime = atoi(line.c_str());

		/* read NA and NB */
		getline(file, line);

		int NA = 0, NB = 0;
		char na[3], nb[3];

		int j = 0;
		na[0] = line.c_str()[j++];
		if(line.c_str()[j] != ' ')
		{
			na[1] = line.c_str()[j++];
			na[2] = '\0';
		}
		else
			na[1] = '\0';

		j++;

		nb[0] = line.c_str()[j++];
		if('0' <= line.c_str()[j] && line.c_str()[j] <= '9')
		{
			nb[1] = line.c_str()[j++];
			nb[2] = '\0';
		}
		else
			nb[1] = '\0';

		NA = atoi(na);
		NB = atoi(nb);

//		int departureA[100], departureB[100];
//		int arrivalA[100], arrivalB[100];
		list<int> departureA, departureB, arrivalA, arrivalB;
		char time[5];

		for(j=0; j<NA; j++)
		{
			getline(file, line);
			time[0] = line.c_str()[0];
			time[1] = line.c_str()[1];
			time[2] = line.c_str()[3];
			time[3] = line.c_str()[4];
			time[4] = '\0';
			departureA.push_back(atoi(time));
			time[0] = line.c_str()[6];
			time[1] = line.c_str()[7];
			time[2] = line.c_str()[9];
			time[3] = line.c_str()[10];
			time[4] = '\0';
			arrivalA.push_back(atoi(time) + turnTime);
		}
		for(j=0; j<NB; j++)
		{
			getline(file, line);
			time[0] = line.c_str()[0];
			time[1] = line.c_str()[1];
			time[2] = line.c_str()[3];
			time[3] = line.c_str()[4];
			time[4] = '\0';
			departureB.push_back(atoi(time));
			time[0] = line.c_str()[6];
			time[1] = line.c_str()[7];
			time[2] = line.c_str()[9];
			time[3] = line.c_str()[10];
			time[4] = '\0';
			arrivalB.push_back(atoi(time) + turnTime);
		}
		departureA.sort();
		departureB.sort();
		arrivalA.sort();
		arrivalB.sort();

		list<int>::iterator k, l;

		/*cout<<"==========="<<endl;
		for(l = departureA.begin(); l != departureA.end(); l++)
			cout << *l << endl;
		cout<<"-----------"<<endl;
		for(l = arrivalA.begin(); l != arrivalA.end(); l++)
			cout << *l << endl;
		cout<<"-----------"<<endl;
		for(l = departureB.begin(); l != departureB.end(); l++)
			cout << *l << endl;
		cout<<"-----------"<<endl;
		for(l = arrivalB.begin(); l != arrivalB.end(); l++)
			cout << *l << endl;
		cout<<"==========="<<endl;
		*/

		for(l=arrivalA.begin(); l!=arrivalA.end(); l++)
		{
			for(k=departureB.begin(); k!=departureB.end(); k++)
			{
				if(*k < *l) continue;
				departureB.erase(k);
				break;
			}
		}

		for(l=arrivalB.begin(); l!=arrivalB.end(); l++)
		{
			for(k=departureA.begin(); k!=departureA.end(); k++)
			{
				if(*k < *l) continue;
				departureA.erase(k);
				break;
			}
		}

		cout << "Case #" << i << ": " << departureA.size() << " " << departureB.size() << endl;
	}

	file.close();

	return 0;
}
