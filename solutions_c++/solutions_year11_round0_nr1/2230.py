#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int T;
  cin >> T;

  for(int i = 0; i < T; i++)
  {
    int N;
    cin >> N;

    vector<int> buttons;
    vector<char> colors;

    vector<int> orange,
		  blue;
    for(int j = 0; j < N; j++)
    {
      char C;
      int button;
      cin >> C >> button;

      buttons.push_back(button);
      colors.push_back(C);

      if(C == 'O')
	orange.push_back(button);
      else
	blue.push_back(button);	
    }

    int posVector = 0;
    int posOrangeVector = 0,
	posBlueVector = 0;

    int posOrange = 1,
	posBlue = 1;

    int time = 0;

    while(posVector < buttons.size())
    {
      bool pushed = false;
      if(posOrangeVector < orange.size())
      {
	if(posOrange != orange[posOrangeVector])
	{
	  posOrange += (posOrange > orange[posOrangeVector] ? -1 : 1);
	}
	else
	{
	  if(colors[posVector] == 'O') // push the button
	  {
	    posVector++;
	    posOrangeVector++;
	    pushed = true;
	  }
	}
      }
      
      if(posBlueVector < blue.size())
      {
	if(posBlue != blue[posBlueVector])
	{
	  posBlue += (posBlue > blue[posBlueVector] ? -1 : 1);
	}
	else
	{
	  if(colors[posVector] == 'B' && !pushed) // push the button
	  {
	    posVector++;
	    posBlueVector++;
	  }
	}
      }


      time++;
    }

    cout << "Case #" << i + 1 << ": " << time << endl;
  }
}
