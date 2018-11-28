#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  ifstream in ("input.txt");
  ofstream out ("answer.txt");
  short num_orange[102], num_blue[102], num_tests, num_buttons, next_blue, next_orange,
        orange_pos, blue_pos;
  char next_color, next;
  unsigned int time;
  bool blue_moved, orange_moved;
  
  in >> num_tests;
  
  for(short j = 0; j < num_tests; j++)
  {
    in >> num_buttons;
    for(short i = 1; i <= num_buttons; i++)
	{
      in >> next_color;
	  //cout << "next color is: ";
	  if(next_color == 'B')
	  {
	    //cout << "blue, next number is: ";
	    in >> num_blue[i];
		//cout << num_blue[i] << endl;
	    num_orange[i] = -1;
	  }
	  else
	  {
	    //cout << "orange, next number is: ";
	    in >> num_orange[i];
		//cout << num_orange[i] << endl;
	    num_blue[i] = -1;
	  }
    }
	if(num_orange[1] == -1)
	{
	  //cout << "blue is first" <<endl;
	  next = 'B';
	}
	else
	{
	  next = 'O';
	}
	orange_pos = 1;
	next_orange = 1;
	blue_pos = 1;
	next_blue = 1;
	time = 0;
	blue_moved = false;
	orange_moved = false;
	while(next_orange <= num_buttons || next_blue <= num_buttons)
	{
	  while(next_orange <= num_buttons && num_orange[next_orange] == -1)
	  {
	    next_orange++;
	  }
	  while(next_blue <= num_buttons && num_blue[next_blue] == -1)
      {
		next_blue++;
      }
	  if(next_orange <= num_buttons && orange_pos != num_orange[next_orange])
	  {
	    if(num_orange[next_orange] < orange_pos)
		{
		  orange_pos--;
		}
		else
		{
		  orange_pos++;
		}
		orange_moved = true;
	  }
	  if(next_blue <= num_buttons && blue_pos != num_blue[next_blue])
	  {
	    if(num_blue[next_blue] < blue_pos)
		{
		  blue_pos--;
		}
		else
		{
		  blue_pos++;
		}
		blue_moved = true;
	  }
	  if(!blue_moved && next_blue <= num_buttons && next == 'B' && blue_pos == num_blue[next_blue])
	  {
	    next_blue++;
		if(next_blue <= num_buttons && num_blue[next_blue] == -1)
		{
		  next = 'O';
		}
	  }
	  else if(!orange_moved && next_orange <= num_buttons && next == 'O' && orange_pos == num_orange[next_orange])
	  {
	    next_orange++;
		if(next_orange <= num_buttons && num_orange[next_orange] == -1)
		{
		  next = 'B';
		}
	  }
	  time++;
	  orange_moved = false;
	  blue_moved = false;
	  //cout << "next_orange: " << next_orange << endl
	  //     << "next_blue: " << next_blue << endl;
	}
	out << "Case #" << j + 1 << ": " << time << endl;
  }
}