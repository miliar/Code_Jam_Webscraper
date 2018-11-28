#include <iostream>
#include <cstring>

using namespace std;

char trans[26];

void buildTrans()
{
	for (int i = 0; i < 26; i++)
	{
		trans[i] = '!';
	}

	const int NUM_SAMPLES = 7;
	char *samplesIn[NUM_SAMPLES];
	char *samplesOut[NUM_SAMPLES];

	samplesIn[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	samplesIn[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	samplesIn[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	samplesIn[3] = "y";
	samplesIn[4] = "e";
	samplesIn[5] = "q";
	samplesIn[6] = "z";

	samplesOut[0] = "our language is impossible to understand";
	samplesOut[1] = "there are twenty six factorial possibilities";
	samplesOut[2] = "so it is okay if you want to just give up";
	samplesOut[3] = "a";
	samplesOut[4] = "o";
	samplesOut[5] = "z";
	samplesOut[6] = "q";


	for (int i = 0; i < NUM_SAMPLES; i++)
	{
		char *sampleIn = samplesIn[i];
		char *sampleOut = samplesOut[i];

		for (int j = 0; j < strlen(sampleIn); j++)
		{
			trans[sampleIn[j] - 'a'] = sampleOut[j];
		}
	}
}

int main()
{
	buildTrans();

	int T;
	cin >> T;
	cin.get();

	for (int i = 0; i < T; i++)
	{
		char line[201];
		cin.getline(line, 200);

		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < strlen(line); j++)
		{
			if (line[j] == ' ') cout << ' ';
			else cout << trans[line[j] - 'a'];
		}
		cout << endl;
	}

	return 0;
}