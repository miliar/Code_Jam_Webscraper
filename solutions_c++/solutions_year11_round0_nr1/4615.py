#include <stdio.h>
#include <string.h>
#include <assert.h>

#include <vector>
using namespace std;

class CMD
{
public:
	char name;
	int distance;
	CMD(char n, int d) { name = n, distance = d; }
	virtual ~CMD(){}
};


class CRobot
{
	enum STATE
	{
		NONE,
		MOVE,
		PUSH,
		STAY,
		LAST
	};
public:
	char name;
	int pos;
	STATE state;

	CRobot(char _n){name = _n, pos = 1, state = STAY ; }
	virtual ~CRobot(){}

	int update(vector<CMD> &v, int ndx)
	{
		if(v[ndx].name == name)
		{
			if(v[ndx].distance == pos)
			{
				//printf("%c : Push button %d\n",name, pos);
				return 1;
			}
			else if(v[ndx].distance > pos )
			{
				pos++;
				//printf("%c : Move button %d\n",name, pos);
			}
			else
			{
				pos--;
				//printf("%c : Move button %d\n",name, pos);
			}
		}
		else
		{
			for(;;)
			{
				ndx++;
				if(v.size()==ndx) return 0;
				if(v[ndx].name==name)
					break;
			}
			if(v[ndx].distance==pos)
			{
				//printf("%c : Stay button %d\n",name, pos);
			}
			else if(v[ndx].distance > pos )
			{
				pos++;
				//printf("%c : Move button %d\n",name, pos);
			}
			else
			{
				pos--;
				//printf("%c : Move button %d\n",name, pos);
			}
		}
		return 0;
	}
};

char *input = "A-large.in";
char *output = "A-large.out";

int main(int argc, char** argv)
{
	int i = 1; // data index
	char buffer[1024] = {0,};

	FILE *in=0,*out=0;
	in = fopen(input,"r");
	out = fopen(output,"w");

	if(in == NULL || out == NULL) return 0;

	fgets(buffer, 1024, in);
	int num = atoi(buffer);
	while(num--)
	{
		CRobot orange('O'), blue('B');
		vector<CMD> cmd;
		int time = 0;
		int ndx = 0; // current command index

		// parsing
		fgets(buffer, 1024, in);

		char *ptr = strtok(buffer," ");
		int len = atoi(ptr);
		while(ptr=strtok(NULL," "))
		{
			char c = ptr[0];
			ptr=strtok(NULL," ");
			char num = atoi(ptr);
			CMD temp(c,num);
			cmd.push_back(temp);
		};

		if(len != (int)cmd.size() )
		{
			assert(0);
		}

		// solve
		for(;;)
		{
			time++;
			int chk1 = orange.update(cmd, ndx);
			int chk2 = blue.update(cmd, ndx);
			if( chk1 || chk2 ) ndx++;
			if(ndx == (int)cmd.size())	break;
			//printf("---------- COUNT : %d\n", time);
		}

		// print
		printf("Case #%d: %d\n",i,time);
		fprintf(out,"Case #%d: %d\n",i,time);

		// finalize
		cmd.clear();
		i++;
	};

	fclose(in);
	fclose(out);
	getchar();
	return 0;
}
