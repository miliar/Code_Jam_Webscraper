
#include "BotTrust.h"

void main()
{

	char filein[] = "A-large.in", fileout[] = "Asmall.out";
	BotTrust obj(filein,fileout);
	obj.MainRun();
}