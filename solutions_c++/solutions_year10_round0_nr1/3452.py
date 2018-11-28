#include "Solver.h"

Solver::Solver(void)
{
	input = fopen("input.txt", "r");
	output = fopen("output.txt", "w");
}

Solver::~Solver(void)
{
	fclose(input);
	fclose(output);
}

void Solver::getInput()
{
	fscanf(input,"%d %d", &n, &k);
}
void Solver::solve()
{
	if (k == 0) 
		on = false;
	else
	{
		n = (1 << n);
		if ((k + 1) % n == 0)
			on = true;
		else 
			on = false;
	}
}
void Solver::writeResult(int j)
{
	if (on)
		fprintf(output,"Case #%d: ON\n", j);
	else 
		fprintf(output,"Case #%d: OFF\n", j);
}
void Solver::close()
{
	fclose(input);
	fclose(output);
}
void Solver::go()
{
	fscanf(input,"%d",&t);
	for (int j = 0; j < t; j++)
	{
		getInput();
		solve();
		writeResult(j + 1);
	}
	close();
}