// Google Codejam 2013 Qualification
// A. Tic Tac Towek
// Author: Paul Cuthbert

#include <iostream>
#include <string>
#include <fstream>
#include <ostream>

const int BOARDSIZE       = 4;
const char PLAYERXSYMBOL  = 'X';
const char PLAYEROSYMBOL  = 'O';
const char EMPTYSQUARE    = '.';
const char NEUTRALPIECE   = 'T';
const std::string inputFilename = "A-small-attempt0.in";
const std::string outputFilename = "output.txt";

std::string gameCondition(const char board[][BOARDSIZE])
{
  std::string gameOutput = "";
  bool gameWon = false;
  bool gameFinished = true;

  for(int i = 0; i < BOARDSIZE; i++)
  {
    if(board[i][0] != NEUTRALPIECE && !gameWon && board[i][0] != EMPTYSQUARE)  // ROW CHECKS
    { 
      if((board[i][0] == board[i][1] || board[i][1] == NEUTRALPIECE) && 
         (board[i][0] == board[i][2] || board[i][2] == NEUTRALPIECE) &&
         (board[i][0] == board[i][3] || board[i][3] == NEUTRALPIECE))
      {
        gameWon = true;
        gameOutput = board[i][0];
      }
    }
    else if(board[i][0] != EMPTYSQUARE && !gameWon)
    {
      if(board[i][1] != EMPTYSQUARE &&
         board[i][1] == board[i][2] &&
         board[i][1] == board[i][3])
      {
        gameWon = true;
        gameOutput = board[i][1];
      }
    }

    if(board[0][i] != NEUTRALPIECE && !gameWon && board[0][i] != EMPTYSQUARE)  // COLUMN CHECKS
    {
      if((board[0][i] == board[1][i] || board[1][i] == NEUTRALPIECE) && 
         (board[0][i] == board[2][i] || board[2][i] == NEUTRALPIECE) &&
         (board[0][i] == board[3][i] || board[3][i] == NEUTRALPIECE))
      {
        gameWon = true;
        gameOutput = board[0][i];
      }
    }
    else if(board[0][i] != EMPTYSQUARE && !gameWon)
    {
      if(board[1][i] != EMPTYSQUARE &&
         board[1][i] == board[2][i] &&
         board[1][i] == board[3][i])
      {
        gameWon = true;
        gameOutput = board[1][i];
      }
    }
  }

  if(!gameWon) // DIAGONAL CHECK 
  {
    if(board[0][0] != NEUTRALPIECE && board[0][0] != EMPTYSQUARE) // Top left - Bottom right
    {
      if((board[0][0] == board[1][1] || board[1][1] == NEUTRALPIECE) &&
         (board[0][0] == board[2][2] || board[2][2] == NEUTRALPIECE) &&
         (board[0][0] == board[3][3] || board[3][3] == NEUTRALPIECE))
      {
        gameWon = true;
        gameOutput = board[0][0];
      }
    }
    else if(board[0][0] != EMPTYSQUARE && !gameWon)
    {
      if(board[1][1] != EMPTYSQUARE &&
         board[1][1] == board[2][2] &&
         board[1][1] == board[3][3])
      {
        gameWon = true;
        gameOutput = board[1][1];
      }
    }

    if(board[0][3] != NEUTRALPIECE && !gameWon && board[0][3] != EMPTYSQUARE) // Top right - Bottom left
    {
      if((board[0][3] == board[2][1] || board[2][1] == NEUTRALPIECE) &&
         (board[0][3] == board[1][2] || board[1][2] == NEUTRALPIECE) &&
         (board[0][3] == board[3][0] || board[3][0] == NEUTRALPIECE))
      {
        gameWon = true;
        gameOutput = board[0][3];
      }
    }
    else if(board[0][3] != EMPTYSQUARE && !gameWon)
    {
      if(board[1][2] != EMPTYSQUARE && 
         board[1][2] == board[2][1] &&
         board[1][2] == board[3][0])
      {
        gameWon = true;
        gameOutput = board[1][2];
      }
    }
  }

  if(!gameWon)
  {
    for(int i = 0; i < BOARDSIZE; i++) // Checks if game is finished
    {
      for(int j = 0; j < BOARDSIZE; j++)
      {
        if(board[i][j] == EMPTYSQUARE)
        {
          gameFinished = false;
        }
      }
    }

    if(!gameFinished)
    {
      gameOutput = "Game has not completed";
    }
    else
    {
      gameOutput = "Draw";
    }
  }
  else
  {
    gameOutput += " won";
  }

  return gameOutput;
}

int main()
{
  char board[BOARDSIZE][BOARDSIZE]; // 2D Board array
  int numberOfTests = 0;
  int currentTest   = 0;
  std::string inputBuffer;
  std::string outputBuffer;

  std::ofstream outputFile;
  std::ifstream inputFile;

  for(int i = 0; i < BOARDSIZE; i++) // Initialise board with emptySquares
  {
    for(int j = 0; j < BOARDSIZE; j++)
    {
      board[i][j] = EMPTYSQUARE;
    }
  }

  inputFile.open(inputFilename);                   // Open input file
  outputFile.open(outputFilename, std::ios::app);  // Open output file
  
  if(inputFile.is_open())
  {
    std::getline(inputFile, inputBuffer);      // Get first line into string buffer
    numberOfTests = atoi(inputBuffer.c_str()); // Get number of tests in file
    inputBuffer.clear();
  }

  if(inputFile.is_open()) 
  {
    while(inputFile.good() && currentTest < numberOfTests)
    {
      std::getline(inputFile, inputBuffer);

      if(!inputFile.eof()) // If not the end of file
      {
        if(!inputBuffer.empty())
        {
          currentTest++;

          for(int i = 0; i < BOARDSIZE; i++)
          {
            for(size_t j = 0; j < inputBuffer.length(); j++)
            {
              board[i][j] = inputBuffer[j];
            }

            inputBuffer.clear();
            std::getline(inputFile, inputBuffer);
          }
        }
      }
      outputBuffer = gameCondition(board);
      outputFile << "Case #" << currentTest << ": " << outputBuffer << std::endl;
    }
  }

  inputFile.close();
  outputFile.close();

  return 0;
}