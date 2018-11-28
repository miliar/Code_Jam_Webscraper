// This file is suitable for small as well as large data sets

//---------------------------------------------------------------------------

#include <stdio.h>

//---------------------------------------------------------------------------

int main()
{
  int N;
  int turnaround;
  int NA, NB;
  int AB_ttable[100][2], BA_ttable[100][2];
  FILE * inFile, * outFile;
  inFile = fopen ("C:\\Documents and Settings\\Risky\\My Documents\\Borland Studio Projects\\train_timetable\\B-large.in","r");
  outFile = fopen ("C:\\Documents and Settings\\Risky\\My Documents\\Borland Studio Projects\\train_timetable\\B-large.out","w");
  if (inFile!=NULL)
  {
	fscanf (inFile, "%d", &N);
	for (int i = 1; i <= N; i++)
	{
		fscanf (inFile, "%d", &turnaround);
		fscanf (inFile, "%d %d", &NA, &NB);

		for (int j = 0; j < NA; j++)
		{
			int temp_minutes;
			fscanf(inFile, "%d", &AB_ttable[j][0]);
			fscanf(inFile, ":");
			fscanf(inFile, "%d", &temp_minutes);
			AB_ttable[j][0] = AB_ttable[j][0] * 60 + temp_minutes;

			fscanf(inFile, "%d", &AB_ttable[j][1]);
			fscanf(inFile, ":");
			fscanf(inFile, "%d", &temp_minutes);
			AB_ttable[j][1] = AB_ttable[j][1] * 60
							+ temp_minutes + turnaround;
/*
			fscanf(inFile, "%d", &AB_ttable[j][2]);
			fscanf(inFile, ":");
			fscanf(inFile, "%d", &AB_ttable[j][3]);

			if (turnaround == 60) AB_ttable[j][2]++;
			else if (turnaround < 60) AB_ttable[j][3] += turnaround;
*/
		}

		for (int j = 0; j < NB; j++)
		{
			int temp_minutes;
			fscanf(inFile, "%d", &BA_ttable[j][0]);
			fscanf(inFile, ":");
			fscanf(inFile, "%d", &temp_minutes);
			BA_ttable[j][0] = BA_ttable[j][0] * 60 + temp_minutes;

			fscanf(inFile, "%d", &BA_ttable[j][1]);
			fscanf(inFile, ":");
			fscanf(inFile, "%d", &temp_minutes);
			BA_ttable[j][1] = BA_ttable[j][1] * 60
							+ temp_minutes + turnaround;
/*
			fscanf(inFile, "%d", &BA_ttable[j][2]);
			fscanf(inFile, ":");
			fscanf(inFile, "%d", &BA_ttable[j][3]);

			if (turnaround == 60) BA_ttable[j][2]++;
			else if (turnaround < 60) BA_ttable[j][3] += turnaround;
*/
		}

		// Sort departures & arrivals idependently, for A & B idependently
		for (int j = 0; j < NA - 1; j++)
		{
			for (int k = j + 1; k < NA; k++)
			{
				int temp;

				if (AB_ttable[j][0] > AB_ttable[k][0])
				{
					temp = AB_ttable[j][0];
					AB_ttable[j][0] = AB_ttable[k][0];
					AB_ttable[k][0] = temp;
				}

				if (AB_ttable[j][1] > AB_ttable[k][1])
				{
					temp = AB_ttable[j][1];
					AB_ttable[j][1] = AB_ttable[k][1];
					AB_ttable[k][1] = temp;
				}

			}
		}

		// Sorting for B
		for (int j = 0; j < NB - 1; j++)
		{
			for (int k = j + 1; k < NB; k++)
			{
				int temp;

				if (BA_ttable[j][0] > BA_ttable[k][0])
				{
					temp = BA_ttable[j][0];
					BA_ttable[j][0] = BA_ttable[k][0];
					BA_ttable[k][0] = temp;
				}

				if (BA_ttable[j][1] > BA_ttable[k][1])
				{
					temp = BA_ttable[j][1];
					BA_ttable[j][1] = BA_ttable[k][1];
					BA_ttable[k][1] = temp;
				}

			}
		}

		int A_trains = NA, B_trains = NB;
		/* Merging A arrivals with B departures
		All links will participate in reduction
		of the number of trains */

		int A_idx = 0, B_idx = 0;
		while ((A_idx < NA) && (B_idx < NB))
		{
			if (AB_ttable[A_idx][1] <= BA_ttable[B_idx][0])
			{
				B_trains--;
				A_idx++;
				B_idx++;
			}
			else
			{
				B_idx++;
			}
		}



		/* Merging A arrivals with B departures
		All links will participate in reduction
		of the number of trains */

		A_idx = 0, B_idx = 0;
		while ((A_idx < NA) && (B_idx < NB))
		{
			if (BA_ttable[B_idx][1] <= AB_ttable[A_idx][0])
			{
				A_trains--;
				A_idx++;
				B_idx++;
			}
			else
			{
				A_idx++;
			}
		}

		fprintf(outFile, "Case #%d: %d %d\n", i, A_trains, B_trains);


	}



	fclose (inFile);
	fclose (outFile);

  }


  return 0;
}
//---------------------------------------------------------------------------
