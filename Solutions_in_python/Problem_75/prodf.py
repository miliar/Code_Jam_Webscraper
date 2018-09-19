class Solve:

    def writeOutput(self, file_name):
        out_file = file(file_name, "w")
        out_file.write(self.invertLines())
        out_file.close()
		
	    def __init__(self, name_file):
        print "Name: ", name_file
        self.arch = file(name_file, "r")
        self.N = int( self.arch.readline())
        print self.N
        self.lines = self.arch.readlines()
        self.arch.close()
    
