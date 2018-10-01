#! /bin/env python

import sys;

class InputFile:
	def __init__(self, filename):
		in_file = open(filename,"r");
		text = in_file.read();
		temp = text.split("\n");
		self.rows = text[len(temp[0]):].split("\n\n");
		self.cases = int(temp[0]);
		in_file.close()

	def getSize(self):
		return self.cases;

	def getBoard(self, number):
		return self.rows[number];

class OutputFile:
	def __init__(self, filename):
		self.filename = filename;
		self.text = "";
	
	def addRow(self, row):
		self.text += row + "\n";
	
	def write(self):
		out_file = open(self.filename,"w");
		out_file.write(self.text);
		out_file.close();

winningRows = { 
			'XXXX' : "X won",
			'TXXX' : "X won",
			'XTXX' : "X won",
			'XXTX' : "X won",
			'XXXT' : "X won",
			'OOOO' : "O won",
			'TOOO' : "O won",
			'OTOO' : "O won",
			'OOTO' : "O won",
			'OOOT' : "O won"
			};


def findWinner(board, column, row):
	isWinner = winningRows.get(board[row:row+4]) or winningRows.get(board[column]+board[column+4]+board[column+8]+board[column+12]);
	if isWinner!=None:
		return isWinner;
	elif column<3:
		return findWinner(board, column+1, row+4);
	else:
		return winningRows.get(board[0]+board[5]+board[10]+board[15]) or winningRows.get(board[3]+board[6]+board[9]+board[12]) or 'Game has not completed' if board.find('.')!=-1 else 'Draw';


if __name__=="__main__":
	inputFileName = sys.argv[1];
	outputFileName = sys.argv[2];
	iFile = InputFile(inputFileName);
	oFile = OutputFile(outputFileName);
	for index in range(0,iFile.getSize()):
		oFile.addRow('Case #' + str(index+1) + ': ' + findWinner(iFile.getBoard(index).replace("\n",""),0,0));
	oFile.write();
