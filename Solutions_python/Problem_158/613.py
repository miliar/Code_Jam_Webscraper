#! /usr/bin/env python3
file_read=open("4a.in","r")
file_write=open("4a.out","w+")
game_status={'1 1 1':'GABRIEL','1 1 2':'GABRIEL','1 1 3':'GABRIEL','1 1 4':'GABRIEL','1 2 1':'GABRIEL','1 2 2':'GABRIEL','1 2 3':'GABRIEL','1 2 4':'GABRIEL',
	'1 3 1':'GABRIEL','1 3 2':'GABRIEL','1 3 3':'GABRIEL','1 3 4':'GABRIEL','1 4 1':'GABRIEL','1 4 2':'GABRIEL','1 4 3':'GABRIEL','1 4 4':'GABRIEL',
	'2 1 1':'RICHARD','2 1 2':'GABRIEL','2 1 3':'RICHARD','2 1 4':'GABRIEL','2 2 1':'GABRIEL','2 2 2':'GABRIEL','2 2 3':'GABRIEL','2 2 4':'GABRIEL',
	'2 3 1':'RICHARD','2 3 2':'GABRIEL','2 3 3':'RICHARD','2 3 4':'GABRIEL','2 4 1':'GABRIEL','2 4 2':'GABRIEL','2 4 3':'GABRIEL','2 4 4':'GABRIEL',
	'3 1 1':'RICHARD','3 1 2':'RICHARD','3 1 3':'RICHARD','3 1 4':'RICHARD','3 2 1':'RICHARD','3 2 2':'RICHARD','3 2 3':'GABRIEL','3 2 4':'RICHARD',
	'3 3 1':'RICHARD','3 3 2':'GABRIEL','3 3 3':'GABRIEL','3 3 4':'GABRIEL','3 4 1':'RICHARD','3 4 2':'RICHARD','3 4 3':'GABRIEL','3 4 4':'RICHARD',
	'4 1 1':'RICHARD','4 1 2':'RICHARD','4 1 3':'RICHARD','4 1 4':'RICHARD','4 2 1':'RICHARD','4 2 2':'RICHARD','4 2 3':'RICHARD','4 2 4':'RICHARD',
	'4 3 1':'RICHARD','4 3 2':'RICHARD','4 3 3':'RICHARD','4 3 4':'GABRIEL','4 4 1':'RICHARD','4 4 2':'RICHARD','4 4 3':'GABRIEL','4 4 4':'GABRIEL'
}
num_cases=int(file_read.readline().strip())
for case_id in range(1,num_cases+1):
	line = file_read.readline().strip();
	solution = str(game_status[line])
	file_write.write("Case #%d: %s\n"%(case_id,solution))
file_read.close();
file_write.close();