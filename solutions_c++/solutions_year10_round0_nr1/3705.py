#include <fstream>

using std::ifstream;
using std::ofstream;

int main(int argc, char* argv[])
{
  if(argc == 1)
  {
    return 0;
  }
  
  ifstream SnapperInput;               // File handle to problems
  ofstream SnapperOutput;              // File handle for output
  unsigned TotalProblems;              // Number of problems in the file
  unsigned Snappers;                   // Number of snappers in the problem
  unsigned Snaps;                      // Number of snaps for the problem
  unsigned SnapperState;               // The state of each snapper ( 1 or 0 )

  char     buffer[255];                // Temp character buffer for file io

  SnapperInput.open(argv[1]);          // Open the problem file

  // Ghetto rename time
  size_t FilePathLength = strlen(argv[1]);
  argv[1][FilePathLength-1] = 't';
  argv[1][FilePathLength-2] = 'o';

  SnapperOutput.open(argv[1], std::ios_base::trunc);         // Open the output file

  if(SnapperInput.is_open() && SnapperOutput.is_open())    // Make sure it opened
  {
    SnapperInput.getline(buffer, 255); // Get the number of problems
    TotalProblems = atoi(buffer);      // Convert it

    for(unsigned Problem = 0; Problem < TotalProblems; ++Problem)
    {
      // Reset our snapper flags to off
      SnapperState = 0;

      // Read in the number of snappers and the number of snaps.
      SnapperInput.get(buffer, 255, ' ');
      Snappers = atoi(buffer);
      SnapperInput.get(buffer, 255, '\n');
      Snaps = atoi(buffer);

      // Start Snapping
      while(Snaps > 0)
      {
        // Snap!
        ++SnapperState;

        // Did we snap passed the number of snappers we have?
        if((SnapperState & (1 << Snappers)) != 0)
        {
          // If so, all the snappers should now be off
          SnapperState = 0;
        }
        --Snaps;
      }
      // We finished snapping, now check to see if the "light" is on

      if(SnapperState == ((1 << Snappers) - 1))
      {
        sprintf_s(buffer, "Case #%i: ON\n", Problem + 1);
        SnapperOutput.write(buffer, strlen(buffer));
      }
      else
      {
        sprintf_s(buffer, "Case #%i: OFF\n", Problem + 1);
        SnapperOutput.write(buffer, strlen(buffer));

      }
      
    }
    SnapperInput.close();
    SnapperOutput.close();
  }

	return 0;
}

