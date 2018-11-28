#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0
#define ARRAYSIZE 204
int Destination ( int *Array, int FromPlace )
{
	while ( Array [FromPlace] != -1 )
	{
		if ( Array [FromPlace] != 0 && Array [FromPlace] != -1 )
			return Array [FromPlace];
		FromPlace++;
	}
	return 0;

};
void NullTheElements ( int *Array )
{
	for ( int i = 0; i < ARRAYSIZE; i++ )
		Array [i] = 0;
};
int main()
{
	FILE *Input, *Output;
	int OrangeButtons [ ARRAYSIZE ], BlueButtons [ ARRAYSIZE ];
	unsigned char InputSymbol = 0, CurrentQueuePosition, CurrentBluePosition, CurrentOrangePosition;
	unsigned char OrangeDestination, BlueDestination, CurrentHer;
	char InputNumber[4];
	int NumberOfTests, NumberOfButtonsToBePressed, Time, Temp, i, j = 0, Result[100];
	bool ButtonPressedThisTime, OrangeTime, BlueTime;
	if ( ( Input = fopen ( "H:\\test.txt", "r" ) ) == 0 )
		return -1;
	fscanf ( Input, "%d", &NumberOfTests );
	while ( ( NumberOfTests-- ) != 0 )
	{
		CurrentQueuePosition = 1;
		CurrentBluePosition = 1;
		CurrentOrangePosition = 1;
		InputSymbol = 0;
		Time = 0;
		NullTheElements ( BlueButtons );
		NullTheElements ( OrangeButtons );
		fscanf ( Input, "%d", &NumberOfButtonsToBePressed );
		Temp = NumberOfButtonsToBePressed;
		while ( NumberOfButtonsToBePressed != 0 )
		{
			InputSymbol = fgetc ( Input );
			if ( InputSymbol == 'B' )
			{
				NumberOfButtonsToBePressed--;
				fgetc ( Input );
				i = 0;
				while ( ( InputNumber[i] = fgetc ( Input ) ) != 32 && InputNumber[i] != 10 && InputNumber[i] != EOF )
					i++;
				ungetc ( InputNumber [i], Input );
				BlueButtons [ CurrentQueuePosition++ ] = atoi ( InputNumber );			
			}
			else if ( InputSymbol == 'O' )
			{
				NumberOfButtonsToBePressed--;
				fgetc ( Input );
				i = 0;
				while ( ( InputNumber[i] = fgetc ( Input ) ) != 32 && InputNumber[i] != 10 )
					i++;
				ungetc ( InputNumber [i], Input );
				OrangeButtons [ CurrentQueuePosition++ ] = atoi ( InputNumber );	
			}
		}
		NumberOfButtonsToBePressed = Temp;
		OrangeButtons [CurrentQueuePosition] = BlueButtons [CurrentQueuePosition] = -1;
		OrangeDestination = 0; 
		BlueDestination = 0;
		CurrentHer = 1;
		BlueTime = FALSE;
		OrangeTime = FALSE;
		while ( NumberOfButtonsToBePressed != 0 )
		{
			Time ++;
			ButtonPressedThisTime = FALSE;
			if ( OrangeTime == FALSE && BlueTime == FALSE )
			{
				if ( OrangeButtons [CurrentHer] != 0 && OrangeButtons [CurrentHer] != -1 )
					OrangeTime = TRUE;
				else if ( BlueButtons [CurrentHer] != 0 && BlueButtons [CurrentHer] != -1 )
					BlueTime = TRUE;
			}
			if ( OrangeDestination == 0 )
				OrangeDestination = Destination ( OrangeButtons, CurrentHer );
			if ( BlueDestination == 0 )
				BlueDestination = Destination ( BlueButtons, CurrentHer );
			if ( CurrentBluePosition > BlueDestination )
				CurrentBluePosition--;
			else if ( CurrentBluePosition < BlueDestination )
				CurrentBluePosition++;
			else 
				if ( ButtonPressedThisTime == FALSE && BlueTime )
				{
					ButtonPressedThisTime = TRUE;
					NumberOfButtonsToBePressed--;
					CurrentHer++;
					BlueDestination = 0;
					BlueTime = FALSE;
				}
			if ( CurrentOrangePosition > OrangeDestination )
				CurrentOrangePosition--;
			else if ( CurrentOrangePosition < OrangeDestination )
				CurrentOrangePosition++;
			else 
				if ( ButtonPressedThisTime == FALSE && OrangeTime )
				{
					ButtonPressedThisTime = TRUE;
					NumberOfButtonsToBePressed--;
					CurrentHer++;
					OrangeDestination = 0;
					OrangeTime = FALSE;
				}
		}
		Result[ j++ ] = Time;	
	}
	fclose ( Input );
	if ( ( Output = fopen ( "H:\\Output.txt", "w" ) ) == 0 )
		return -1;
	for ( i = 0; i < j; i++ )
	{
		fprintf ( Output, "Case #%d: %d\n", i+1, Result[i]);
	}
	fclose ( Output );
	return 0;
}